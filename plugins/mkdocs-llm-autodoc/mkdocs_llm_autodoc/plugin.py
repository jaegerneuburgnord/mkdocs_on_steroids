"""
MkDocs LLM AutoDoc Plugin

This plugin automatically generates multi-level documentation for C++ projects using LLMs.
"""

import os
import logging
import threading
import time
from pathlib import Path
from typing import Any, Dict, List
from concurrent.futures import ThreadPoolExecutor, as_completed

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from mkdocs.config.defaults import MkDocsConfig

try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False
    # Fallback: Simple progress indicator
    class tqdm:
        def __init__(self, iterable=None, total=None, desc=None, **kwargs):
            self.iterable = iterable
            self.total = total or (len(iterable) if iterable else 0)
            self.desc = desc
            self.n = 0
            if desc:
                print(f"{desc}: 0/{self.total}")

        def __iter__(self):
            for item in self.iterable:
                yield item
                self.update(1)

        def update(self, n=1):
            self.n += n
            if self.desc and self.n % max(1, self.total // 20) == 0:  # Update every 5%
                print(f"{self.desc}: {self.n}/{self.total}")

        def __enter__(self):
            return self

        def __exit__(self, *args):
            if self.desc:
                print(f"{self.desc}: {self.n}/{self.total} - Complete!")

from .agents.high_level_agent import HighLevelAgent
from .agents.mid_level_agent import MidLevelAgent
from .agents.detailed_level_agent import DetailedLevelAgent
from .parsers.cpp_parser import CppParser
from .utils.cache_manager import CacheManager
from .utils.cross_reference import CrossReferenceManager
from .utils.llm_provider import LLMProviderFactory

logger = logging.getLogger('mkdocs.plugins.llm-autodoc')


class LLMAutoDocPluginConfig(config_options.Config):
    """Configuration options for the LLM AutoDoc plugin"""

    # Required settings
    enabled = config_options.Type(bool, default=True)
    cpp_project_path = config_options.Type(str, default='.')

    # LLM Configuration
    llm_provider = config_options.Choice(['anthropic', 'openai', 'ollama', 'lmstudio'], default='anthropic')
    llm_api_key = config_options.Type(str, default=None)
    llm_model = config_options.Type(str, default='claude-3-5-sonnet-20241022')
    llm_base_url = config_options.Type(str, default=None)  # For Ollama, LM Studio, or custom endpoints
    llm_timeout = config_options.Type(float, default=600.0)  # Timeout in seconds (default: 10 minutes)

    # Documentation levels to generate
    generate_high_level = config_options.Type(bool, default=True)
    generate_mid_level = config_options.Type(bool, default=True)
    generate_detailed_level = config_options.Type(bool, default=True)

    # Output paths
    high_level_output = config_options.Type(str, default='generated')
    mid_level_output = config_options.Type(str, default='generated/modules')
    detailed_level_output = config_options.Type(str, default='generated/api')

    # Caching
    enable_cache = config_options.Type(bool, default=True)
    cache_dir = config_options.Type(str, default='.cache/llm-autodoc')
    force_regenerate = config_options.Type(bool, default=False)

    # Quality control
    enable_quality_check = config_options.Type(bool, default=True)
    enable_cross_references = config_options.Type(bool, default=True)
    enable_code_review = config_options.Type(bool, default=True)

    # File patterns
    include_patterns = config_options.Type(list, default=['**/*.h', '**/*.hpp', '**/*.cpp'])
    exclude_patterns = config_options.Type(list, default=['**/build/**', '**/third_party/**', '**/external/**'])

    # Advanced
    max_concurrent_llm_calls = config_options.Type(int, default=3)
    retry_failed = config_options.Type(bool, default=True)
    verbose = config_options.Type(bool, default=False)

    # Background processing
    background_generation = config_options.Type(bool, default=True)
    show_generation_progress = config_options.Type(bool, default=True)


class LLMAutoDocPlugin(BasePlugin[LLMAutoDocPluginConfig]):
    """
    MkDocs plugin that generates intelligent multi-level C++ documentation using LLMs.

    This plugin provides three levels of documentation:
    1. High-Level: Project overview, architecture, entry points
    2. Mid-Level: Module documentation with classes and dependencies
    3. Detailed-Level: Complete API documentation with examples
    """

    def __init__(self):
        super().__init__()
        self.cache_manager = None
        self.cpp_parser = None
        self.cross_ref_manager = None
        self.llm_provider = None

        self.high_level_agent = None
        self.mid_level_agent = None
        self.detailed_agent = None

        self.generated_files = []
        self.generation_thread = None
        self.generation_complete = threading.Event()
        self.files_lock = threading.Lock()

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig:
        """
        Called when the config is loaded. Initialize all components.
        """
        if not self.config.enabled:
            logger.info("LLM AutoDoc plugin is disabled")
            return config

        # Validate configuration
        if not self.config.llm_api_key and self.config.llm_provider not in ['ollama', 'lmstudio']:
            logger.warning(
                "No LLM API key provided. Set llm_api_key in mkdocs.yml or "
                "use environment variable (ANTHROPIC_API_KEY or OPENAI_API_KEY)"
            )
            # Try to get from environment
            if self.config.llm_provider == 'anthropic':
                self.config.llm_api_key = os.getenv('ANTHROPIC_API_KEY')
            elif self.config.llm_provider == 'openai':
                self.config.llm_api_key = os.getenv('OPENAI_API_KEY')

        # Initialize components
        docs_dir = Path(config['docs_dir'])
        cache_dir = Path(self.config.cache_dir)
        cache_dir.mkdir(parents=True, exist_ok=True)

        self.cache_manager = CacheManager(cache_dir, enabled=self.config.enable_cache)
        self.cpp_parser = CppParser(
            include_patterns=self.config.include_patterns,
            exclude_patterns=self.config.exclude_patterns
        )
        self.cross_ref_manager = CrossReferenceManager()

        # Initialize LLM provider
        try:
            self.llm_provider = LLMProviderFactory.create(
                provider=self.config.llm_provider,
                api_key=self.config.llm_api_key,
                model=self.config.llm_model,
                base_url=self.config.llm_base_url,
                timeout=self.config.llm_timeout
            )
        except Exception as e:
            logger.error(f"Failed to initialize LLM provider: {e}")
            return config

        # Initialize agents
        self.high_level_agent = HighLevelAgent(
            llm_provider=self.llm_provider,
            cache_manager=self.cache_manager
        )
        self.mid_level_agent = MidLevelAgent(
            llm_provider=self.llm_provider,
            cache_manager=self.cache_manager,
            cross_ref_manager=self.cross_ref_manager
        )
        self.detailed_agent = DetailedLevelAgent(
            llm_provider=self.llm_provider,
            cache_manager=self.cache_manager,
            cross_ref_manager=self.cross_ref_manager
        )

        logger.info(f"LLM AutoDoc plugin initialized with {self.config.llm_provider}/{self.config.llm_model}")

        return config

    def _generate_documentation_sync(self, config: MkDocsConfig):
        """
        Internal method that performs the actual documentation generation.
        Can be called synchronously or in a background thread.
        """
        try:
            # Parse C++ project
            project_path = Path(self.config.cpp_project_path)
            if not project_path.exists():
                logger.error(f"C++ project path not found: {project_path}")
                return

            logger.info(f"Parsing C++ project at: {project_path}")
            project_structure = self.cpp_parser.parse_project_structure(str(project_path))

            # Detect changed files
            if self.config.force_regenerate:
                changed_files = project_structure['all_files']
                logger.info("Force regenerate enabled - processing all files")
            else:
                changed_files = self.cache_manager.detect_changed_files(
                    str(project_path),
                    project_structure['all_files']
                )
                logger.info(f"Detected {len(changed_files)} changed files")

            docs_dir = Path(config['docs_dir'])

            # Track successfully processed files for cache update
            successfully_processed_files = []

            # Generate High-Level Documentation
            if self.config.generate_high_level:
                logger.info("Generating high-level documentation...")
                output_dir = docs_dir / self.config.high_level_output
                output_dir.mkdir(parents=True, exist_ok=True)

                high_level_files = self.high_level_agent.generate(
                    project_structure=project_structure,
                    output_dir=str(output_dir)
                )
                with self.files_lock:
                    self.generated_files.extend(high_level_files)
                logger.info(f"✓ Generated {len(high_level_files)} high-level documentation files")

            # Generate Mid-Level Documentation
            if self.config.generate_mid_level and project_structure['modules']:
                logger.info("Generating mid-level module documentation...")
                output_dir = docs_dir / self.config.mid_level_output
                output_dir.mkdir(parents=True, exist_ok=True)

                mid_level_files = []
                modules_to_process = [
                    module for module in project_structure['modules']
                    if any(f in changed_files for f in module['files']) or self.config.force_regenerate
                ]

                desc = "📦 Generating Module Docs" if self.config.show_generation_progress else None
                for module in tqdm(modules_to_process, desc=desc, unit="module", disable=not self.config.show_generation_progress):
                    try:
                        files = self.mid_level_agent.generate(
                            module=module,
                            project_structure=project_structure,
                            output_dir=str(output_dir)
                        )
                        mid_level_files.extend(files)
                        # Mark module files as successfully processed
                        successfully_processed_files.extend(module['files'])
                    except Exception as e:
                        logger.error(f"Failed to generate mid-level docs for module {module.get('name', 'unknown')}: {e}")

                # Log skipped modules
                skipped = len(project_structure['modules']) - len(modules_to_process)
                if skipped > 0:
                    logger.info(f"Skipped {skipped} unchanged modules (using cache)")

                with self.files_lock:
                    self.generated_files.extend(mid_level_files)
                logger.info(f"✓ Generated {len(mid_level_files)} module documentation files")

            # Generate Detailed API Documentation
            if self.config.generate_detailed_level:
                logger.info("Generating detailed API documentation...")
                output_dir = docs_dir / self.config.detailed_level_output
                output_dir.mkdir(parents=True, exist_ok=True)

                files_to_document = changed_files if not self.config.force_regenerate else project_structure['all_files']
                detailed_files = []

                # Helper function for parallel processing
                def process_file(file_path):
                    file_info = self.cpp_parser.parse_file(file_path)
                    if file_info and (file_info.get('classes') or file_info.get('functions')):
                        try:
                            files = self.detailed_agent.generate(
                                file_info=file_info,
                                project_structure=project_structure,
                                output_dir=str(output_dir)
                            )
                            return files, None, file_path
                        except Exception as e:
                            if self.config.retry_failed:
                                try:
                                    files = self.detailed_agent.generate(
                                        file_info=file_info,
                                        project_structure=project_structure,
                                        output_dir=str(output_dir)
                                    )
                                    return files, None, file_path
                                except Exception as retry_error:
                                    return None, retry_error, file_path
                            return None, e, file_path
                    return None, None, file_path

                # Use ThreadPoolExecutor for parallel processing with tqdm
                max_workers = self.config.max_concurrent_llm_calls
                logger.info(f"Processing {len(files_to_document)} files with {max_workers} parallel workers")

                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    # Submit all tasks
                    futures = {executor.submit(process_file, fp): fp for fp in files_to_document}

                    # Process completed tasks with tqdm progress bar
                    desc = "📄 Generating API Docs" if self.config.show_generation_progress else None
                    with tqdm(total=len(files_to_document), desc=desc, unit="file", disable=not self.config.show_generation_progress) as pbar:
                        for future in as_completed(futures):
                            file_path = futures[future]
                            try:
                                files, error, processed_path = future.result()
                                if files:
                                    detailed_files.extend(files)
                                    # Immediately add to generated_files so they can be picked up
                                    with self.files_lock:
                                        self.generated_files.extend(files)
                                    # Mark file as successfully processed for cache update
                                    successfully_processed_files.append(processed_path)
                                if error:
                                    logger.error(f"Failed to generate documentation for {processed_path}: {error}")
                            except Exception as exc:
                                logger.error(f"Exception processing {file_path}: {exc}")
                            finally:
                                pbar.update(1)

                logger.info(f"✓ Generated {len(detailed_files)} API documentation files")

            # Update cross-references
            if self.config.enable_cross_references:
                logger.info("Updating cross-references...")
                with self.files_lock:
                    self.cross_ref_manager.update_references(str(docs_dir), self.generated_files.copy())

            # Update cache - ONLY for successfully processed files
            # This prevents failed files from being marked as "processed" in the cache
            if successfully_processed_files:
                # Remove duplicates while preserving order
                unique_processed_files = list(dict.fromkeys(successfully_processed_files))
                logger.info(f"Updating cache for {len(unique_processed_files)} successfully processed files")
                self.cache_manager.update_cache(
                    str(project_path),
                    unique_processed_files
                )
            else:
                logger.info("No files were successfully processed - cache not updated")

            with self.files_lock:
                total_files = len(self.generated_files)
            logger.info(f"✅ Documentation generation complete! Generated {total_files} files")

        except Exception as e:
            logger.error(f"Error during documentation generation: {e}", exc_info=True)
        finally:
            self.generation_complete.set()

    def on_pre_build(self, config: MkDocsConfig) -> None:
        """
        Called before the build starts. Start documentation generation here.
        """
        if not self.config.enabled or not self.llm_provider:
            return

        logger.info("Starting LLM-powered documentation generation...")

        # Check if there are already generated files (from a previous run)
        docs_dir = Path(config['docs_dir'])
        existing_files = []
        for output_dir in [self.config.high_level_output, self.config.mid_level_output, self.config.detailed_level_output]:
            gen_dir = docs_dir / output_dir
            if gen_dir.exists():
                existing_files.extend([str(f) for f in gen_dir.rglob('*.md')])

        if existing_files:
            logger.info(f"📚 Found {len(existing_files)} existing documentation files - they will be available immediately")

        # Start generation in background or synchronously
        if self.config.background_generation:
            logger.info("🚀 Starting background documentation generation...")
            logger.info("📝 New documentation will appear automatically as it's generated")
            self.generation_thread = threading.Thread(
                target=self._generate_documentation_sync,
                args=(config,),
                daemon=True,
                name="LLMAutoDocGenerator"
            )
            self.generation_thread.start()
        else:
            logger.info("Starting synchronous documentation generation...")
            self._generate_documentation_sync(config)

    def on_files(self, files: Files, config: MkDocsConfig) -> Files:
        """
        Called after files are collected. Add generated files to the build.
        """
        if not self.config.enabled:
            return files

        # Generated files are already in the docs directory, so they will be
        # picked up automatically by MkDocs
        return files

    def on_post_build(self, config: MkDocsConfig) -> None:
        """
        Called after the build is complete.
        """
        if not self.config.enabled:
            return

        with self.files_lock:
            num_files = len(self.generated_files)

        if self.config.background_generation and self.generation_thread and self.generation_thread.is_alive():
            logger.info(f"📄 Build complete with {num_files} generated files so far")
            logger.info("⏳ Background documentation generation is still running...")
            logger.info("💡 New files will appear automatically in your browser as they're generated")
        else:
            logger.info(f"✅ Build complete with {num_files} generated files")
