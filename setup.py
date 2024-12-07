from setuptools import setup, find_packages

setup(
    name="crawler",
    version="0.1.0",
    description="A dynamic web crawler with semantic search capabilities",
    author="Derek Sun",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "selenium",
        "sentence-transformers",
        "numpy",
    ],
    python_requires=">=3.7",
)
