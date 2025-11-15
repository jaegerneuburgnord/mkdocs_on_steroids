import os
from setuptools import setup, find_packages

setup(
    name='mkdocs-llm-autodoc',
    version='1.0.0',
    description='MkDocs plugin for intelligent multi-level C++ code documentation using LLMs',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    keywords='mkdocs python plugin documentation llm cpp',
    url='',
    author='',
    author_email='',
    license='MIT',
    python_requires='>=3.8',
    install_requires=[
        'mkdocs>=1.4.0',
        'anthropic>=0.18.0',
        'openai>=1.0.0',
        'tree-sitter>=0.21.0',
        'tree-sitter-cpp>=0.21.0',
        'pyyaml>=6.0',
        'jinja2>=3.0.0',
        'watchdog>=3.0.0',
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'llm-autodoc = mkdocs_llm_autodoc.plugin:LLMAutoDocPlugin',
        ]
    },
    include_package_data=True,
    package_data={
        'mkdocs_llm_autodoc': ['templates/*.md'],
    },
)
