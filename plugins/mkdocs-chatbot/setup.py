"""
Setup configuration for mkdocs-chatbot plugin
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mkdocs-chatbot",
    version="1.0.0",
    description="An OpenAI-powered chatbot plugin for MkDocs documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/mkdocs-chatbot",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'mkdocs_chatbot': [
            'assets/*.js',
            'assets/*.css',
        ],
    },
    install_requires=[
        'mkdocs>=1.4.0',
    ],
    entry_points={
        'mkdocs.plugins': [
            'chatbot = mkdocs_chatbot.plugin:ChatBotPlugin',
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Documentation",
        "Topic :: Text Processing :: Markup :: Markdown",
    ],
    python_requires=">=3.8",
    keywords="mkdocs plugin chatbot openai documentation ai assistant",
)
