"""
High-Level Documentation Agent

Generates project overview and architecture documentation.
Creates 300-word introductions with architecture diagrams.
"""

import logging
from pathlib import Path
from typing import Dict, List, Any

logger = logging.getLogger('mkdocs.plugins.llm-autodoc.high-level')


class HighLevelAgent:
    """
    Agent for generating high-level project documentation.

    Creates:
    - Project overview (00-getting-started.md)
    - Architecture documentation (01-architecture.md)
    - Technology stack overview
    - Entry points for new developers
    """

    def __init__(self, llm_provider, cache_manager):
        self.llm = llm_provider
        self.cache = cache_manager

    def generate(self, project_structure: Dict[str, Any], output_dir: str) -> List[str]:
        """
        Generate high-level documentation files.

        Args:
            project_structure: Parsed C++ project structure
            output_dir: Directory to write documentation files

        Returns:
            List of generated file paths
        """
        generated_files = []
        output_path = Path(output_dir)

        # Generate Getting Started
        getting_started_file = output_path / '00-getting-started.md'
        content = self._generate_getting_started(project_structure)
        getting_started_file.write_text(content, encoding='utf-8')
        generated_files.append(str(getting_started_file))
        logger.info(f"Generated: {getting_started_file}")

        # Generate Architecture Documentation
        architecture_file = output_path / '01-architecture.md'
        content = self._generate_architecture(project_structure)
        architecture_file.write_text(content, encoding='utf-8')
        generated_files.append(str(architecture_file))
        logger.info(f"Generated: {architecture_file}")

        return generated_files

    def _generate_getting_started(self, project_structure: Dict[str, Any]) -> str:
        """Generate getting started documentation"""

        prompt = self._build_getting_started_prompt(project_structure)

        # Check cache
        cache_key = f"high_level_getting_started_{hash(str(project_structure))}"
        cached = self.cache.get(cache_key)
        if cached:
            logger.info("Using cached getting started documentation")
            return cached

        # Generate with LLM
        response = self.llm.generate(prompt)

        # Cache result
        self.cache.set(cache_key, response)

        return response

    def _generate_architecture(self, project_structure: Dict[str, Any]) -> str:
        """Generate architecture documentation"""

        prompt = self._build_architecture_prompt(project_structure)

        # Check cache
        cache_key = f"high_level_architecture_{hash(str(project_structure))}"
        cached = self.cache.get(cache_key)
        if cached:
            logger.info("Using cached architecture documentation")
            return cached

        # Generate with LLM
        response = self.llm.generate(prompt)

        # Cache result
        self.cache.set(cache_key, response)

        return response

    def _build_getting_started_prompt(self, project_structure: Dict[str, Any]) -> str:
        """Build prompt for getting started documentation"""

        structure_summary = self._summarize_structure(project_structure)

        prompt = f"""Analyze this C++ project structure and create a comprehensive getting started guide.

# Project Structure
{structure_summary}

# Your Task
Create a 300-word introduction that includes:

1. **Main Purpose**: What is this project for? What problems does it solve?
2. **Core Architecture**: Identify 3-5 main components/modules and briefly describe each
3. **Entry Points for New Developers**:
   - Where should a new developer start reading the code?
   - Which are the most important files/classes to understand first?
   - Common workflows or usage patterns
4. **Technology Stack**:
   - C++ standard version used
   - Key libraries and dependencies
   - Build system (CMake, Make, etc.)
   - Testing framework

# Output Format
Generate a complete Markdown document with:
- Clear headings
- Bullet points for easy scanning
- A Mermaid diagram showing the high-level architecture
- Code examples if relevant
- Links to important files (use relative paths)

# Example Mermaid Diagram
```mermaid
graph TB
    A[Main Application] --> B[Core Library]
    A --> C[Utilities]
    B --> D[Data Structures]
    B --> E[Algorithms]
```

Write in a clear, welcoming tone for developers new to the project.
Generate ONLY the markdown content, no additional commentary.
"""
        return prompt

    def _build_architecture_prompt(self, project_structure: Dict[str, Any]) -> str:
        """Build prompt for architecture documentation"""

        structure_summary = self._summarize_structure(project_structure)
        modules = project_structure.get('modules', [])
        dependencies = project_structure.get('dependencies', {})

        prompt = f"""Analyze this C++ project and create comprehensive architecture documentation.

# Project Structure
{structure_summary}

# Modules
{self._format_modules(modules)}

# Dependencies
{self._format_dependencies(dependencies)}

# Your Task
Create detailed architecture documentation covering:

1. **Architecture Overview** (150 words)
   - High-level architectural pattern (monolithic, layered, microservices-style, etc.)
   - Design principles evident in the codebase
   - Key architectural decisions

2. **Component Breakdown**
   - For each major component/module:
     - Purpose and responsibilities
     - Key classes and interfaces
     - Interactions with other components

3. **Data Flow**
   - How data moves through the system
   - Key data structures
   - Data transformation points

4. **Design Patterns**
   - Identify design patterns used (Factory, Singleton, Observer, etc.)
   - Where and why they're applied

5. **Threading and Concurrency** (if applicable)
   - Threading model
   - Synchronization mechanisms
   - Concurrent data structures

# Output Format
Generate a complete Markdown document with:
- Multiple Mermaid diagrams (architecture, data flow, component relationships)
- Clear sections with headings
- Code snippets showing key patterns
- Cross-references to detailed documentation

Example diagrams:
```mermaid
flowchart LR
    User[User Input] --> Parser[Parser]
    Parser --> Validator[Validator]
    Validator --> Executor[Executor]
    Executor --> Output[Output Handler]
```

Generate ONLY the markdown content, no additional commentary.
"""
        return prompt

    def _summarize_structure(self, project_structure: Dict[str, Any]) -> str:
        """Create a text summary of the project structure"""
        lines = []

        lines.append(f"**Total Files**: {len(project_structure.get('all_files', []))}")
        lines.append(f"**Modules**: {len(project_structure.get('modules', []))}")

        # File types
        headers = len([f for f in project_structure.get('all_files', []) if f.endswith(('.h', '.hpp'))])
        sources = len([f for f in project_structure.get('all_files', []) if f.endswith('.cpp')])
        lines.append(f"**Header Files**: {headers}")
        lines.append(f"**Source Files**: {sources}")

        # Directory structure
        if 'directory_tree' in project_structure:
            lines.append("\n**Directory Structure**:")
            lines.append("```")
            lines.append(project_structure['directory_tree'])
            lines.append("```")

        return '\n'.join(lines)

    def _format_modules(self, modules: List[Dict]) -> str:
        """Format modules for the prompt"""
        if not modules:
            return "No modules identified"

        lines = []
        for module in modules:
            lines.append(f"- **{module['name']}**: {len(module.get('files', []))} files")
            if module.get('path'):
                lines.append(f"  - Path: `{module['path']}`")

        return '\n'.join(lines)

    def _format_dependencies(self, dependencies: Dict) -> str:
        """Format dependencies for the prompt"""
        if not dependencies:
            return "No external dependencies identified"

        lines = []
        for dep_type, deps in dependencies.items():
            lines.append(f"**{dep_type}**: {', '.join(deps)}")

        return '\n'.join(lines)
