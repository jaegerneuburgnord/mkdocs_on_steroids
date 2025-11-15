"""
MkDocs Integrator

Automatically updates mkdocs.yml configuration to include generated documentation.
"""

import logging
import yaml
from pathlib import Path
from typing import Dict, List, Any

logger = logging.getLogger('mkdocs.plugins.llm-autodoc.integrator')


class MkDocsIntegrator:
    """
    Handles integration with MkDocs configuration.

    Automatically adds generated documentation files to the nav structure.
    """

    def __init__(self):
        pass

    def update_config(self, docs_dir: str, results: Dict[str, List[str]]):
        """
        Update MkDocs configuration to include generated files.

        Args:
            docs_dir: Documentation directory
            results: Dictionary with generated files (high_level, mid_level, detailed)
        """
        # For now, this is handled by MkDocs automatically
        # Files in the docs directory are automatically discovered

        logger.info("MkDocs will automatically discover generated documentation files")

        # Optional: We could update mkdocs.yml here to add explicit nav entries
        # But it's usually better to let MkDocs auto-discover files

    def create_index(self, docs_dir: str, results: Dict[str, List[str]]):
        """
        Create an index page linking to all generated documentation.

        Args:
            docs_dir: Documentation directory
            results: Dictionary with generated files
        """
        docs_path = Path(docs_dir)
        index_file = docs_path / 'generated' / 'index.md'

        index_content = self._build_index_content(results)

        index_file.parent.mkdir(parents=True, exist_ok=True)
        index_file.write_text(index_content, encoding='utf-8')

        logger.info(f"Created index page: {index_file}")

    def _build_index_content(self, results: Dict[str, List[str]]) -> str:
        """Build content for the index page"""
        lines = [
            "# Generated Documentation",
            "",
            "This documentation was automatically generated using LLM-powered analysis.",
            "",
        ]

        # High-level docs
        if results.get('highLevel'):
            lines.append("## Architecture & Overview")
            lines.append("")
            for file_path in results['highLevel']:
                file_name = Path(file_path).stem
                title = file_name.replace('-', ' ').title()
                lines.append(f"- [{title}]({file_name}.md)")
            lines.append("")

        # Mid-level docs
        if results.get('midLevel'):
            lines.append("## Module Documentation")
            lines.append("")
            for file_path in results['midLevel']:
                file_name = Path(file_path).stem
                title = file_name.replace('-', ' ').title()
                lines.append(f"- [{title}](modules/{file_name}.md)")
            lines.append("")

        # Detailed docs
        if results.get('detailed'):
            lines.append("## API Reference")
            lines.append("")
            lines.append("### Classes")
            lines.append("")

            for file_path in results['detailed']:
                if 'classes' in file_path:
                    file_name = Path(file_path).stem
                    title = file_name.replace('-', ' ').title()
                    lines.append(f"- [{title}](api/classes/{file_name}.md)")

            lines.append("")
            lines.append("### Functions")
            lines.append("")

            for file_path in results['detailed']:
                if 'functions' in file_path:
                    file_name = Path(file_path).stem
                    title = file_name.replace('-', ' ').title()
                    lines.append(f"- [{title}](api/functions/{file_name}.md)")

        return '\n'.join(lines)
