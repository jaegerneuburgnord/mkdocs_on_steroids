"""
Cross-Reference Manager

Creates and manages links between different documentation levels:
- High-level -> Mid-level
- Mid-level -> Detailed-level
- Cross-references between modules and classes
"""

import re
import logging
from pathlib import Path
from typing import Dict, List, Set, Any

logger = logging.getLogger('mkdocs.plugins.llm-autodoc.crossref')


class CrossReferenceManager:
    """
    Manages cross-references between documentation files.

    Automatically creates links between:
    - Module documentation and class documentation
    - Class documentation and related classes
    - High-level architecture docs and module docs
    """

    def __init__(self):
        self.modules = {}  # module_name -> documentation content
        self.classes = {}  # class_name -> documentation content
        self.functions = {}  # function_name -> documentation content

        self.module_to_classes = {}  # module_name -> [class_names]
        self.class_to_module = {}  # class_name -> module_name

    def register_module(self, module_name: str, content: str):
        """Register a module and its documentation"""
        self.modules[module_name] = content
        logger.debug(f"Registered module: {module_name}")

    def register_class(self, class_name: str, content: str, module_name: str = None):
        """Register a class and its documentation"""
        self.classes[class_name] = content

        if module_name:
            self.class_to_module[class_name] = module_name

            if module_name not in self.module_to_classes:
                self.module_to_classes[module_name] = []
            self.module_to_classes[module_name].append(class_name)

        logger.debug(f"Registered class: {class_name}")

    def register_function(self, function_name: str, content: str):
        """Register a function and its documentation"""
        self.functions[function_name] = content
        logger.debug(f"Registered function: {function_name}")

    def update_references(self, docs_dir: str, generated_files: List[str]):
        """
        Update cross-references in all generated documentation files.

        Args:
            docs_dir: Documentation directory
            generated_files: List of generated file paths
        """
        logger.info("Updating cross-references...")

        for file_path in generated_files:
            try:
                self._update_file_references(file_path, docs_dir)
            except Exception as e:
                logger.warning(f"Error updating references in {file_path}: {e}")

        logger.info(f"Updated cross-references in {len(generated_files)} files")

    def _update_file_references(self, file_path: str, docs_dir: str):
        """Update references in a single file"""
        file_path = Path(file_path)

        if not file_path.exists():
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all class names mentioned in the content
        modified = content

        # Create links for class names
        for class_name in self.classes.keys():
            # Look for mentions of the class name that aren't already links
            pattern = r'\b' + re.escape(class_name) + r'\b(?!\])'

            def replace_class_mention(match):
                # Don't replace if it's already in a link or code block
                start = max(0, match.start() - 10)
                context = modified[start:match.start()]

                if '[' in context or '`' in context:
                    return match.group(0)

                # Create relative link
                rel_path = self._get_relative_link(file_path, class_name, 'class', docs_dir)
                return f"[{class_name}]({rel_path})"

            # Only replace first few occurrences to avoid cluttering
            matches = list(re.finditer(pattern, modified))
            for match in matches[:3]:  # Limit to first 3 mentions
                modified = modified[:match.start()] + replace_class_mention(match) + modified[match.end():]

        # Create links for module names
        for module_name in self.modules.keys():
            pattern = r'\b' + re.escape(module_name) + r'\s+module\b'

            def replace_module_mention(match):
                rel_path = self._get_relative_link(file_path, module_name, 'module', docs_dir)
                return f"[{module_name} module]({rel_path})"

            modified = re.sub(pattern, replace_module_mention, modified, count=3)

        # Only write if content changed
        if modified != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified)
            logger.debug(f"Updated references in: {file_path}")

    def _get_relative_link(self, from_file: Path, target_name: str, target_type: str, docs_dir: str) -> str:
        """
        Generate a relative link from one file to another.

        Args:
            from_file: Source file path
            target_name: Name of target (class, module, etc.)
            target_type: Type of target ('class', 'module', 'function')
            docs_dir: Documentation directory

        Returns:
            Relative link path
        """
        docs_dir = Path(docs_dir)

        # Determine target file path
        if target_type == 'class':
            target_file = docs_dir / 'generated' / 'api' / 'classes' / f"{self._sanitize_filename(target_name)}.md"
        elif target_type == 'module':
            target_file = docs_dir / 'generated' / 'modules' / f"{self._sanitize_filename(target_name)}.md"
        elif target_type == 'function':
            target_file = docs_dir / 'generated' / 'api' / 'functions' / f"{self._sanitize_filename(target_name)}.md"
        else:
            return '#'

        # Calculate relative path
        try:
            rel_path = target_file.relative_to(from_file.parent)
            return str(rel_path).replace('\\', '/')
        except ValueError:
            # Files are on different drives or can't calculate relative path
            try:
                rel_path = target_file.relative_to(docs_dir)
                return '/' + str(rel_path).replace('\\', '/')
            except ValueError:
                return '#'

    def _sanitize_filename(self, name: str) -> str:
        """Convert name to safe filename"""
        safe = name.lower()
        safe = safe.replace('::', '-')
        safe = safe.replace(' ', '-')
        safe = safe.replace('_', '-')
        safe = ''.join(c for c in safe if c.isalnum() or c == '-')
        return safe

    def get_related_classes(self, class_name: str) -> List[str]:
        """Get classes related to the given class"""
        related = []

        # Find classes in the same module
        module = self.class_to_module.get(class_name)
        if module and module in self.module_to_classes:
            related = [c for c in self.module_to_classes[module] if c != class_name]

        return related

    def get_module_classes(self, module_name: str) -> List[str]:
        """Get all classes in a module"""
        return self.module_to_classes.get(module_name, [])
