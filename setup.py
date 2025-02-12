from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='summarizer',
    version='0.1dev0',
    author='Renato Rodrigues', 
    author_email='spamcares-github@yahoo.com',
    description='Leverage of LLM to summarize content',
    url='https://github.com/rs-renato/llm-summarizer',
    keywords=['llm', 'summarization', 'ai', 'ollama'],
    packages=find_packages(where="summarizer"),
    package_dir={"": "summarizer"},
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "summarize=main:app",
        ]
    },
    python_requires=">=3.11"
)