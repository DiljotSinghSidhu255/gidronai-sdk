from setuptools import setup, find_packages
setup(
    name="gidronai",
    version="0.3.1",
    description="Python SDK for GidronAI Synthetic Reality Engine",
    author="Diljot Singh Sidhu",
    author_email="diljot@gidronai.me",
    url="https://github.com/DiljotSinghSidhu255/gidronai-sdk",
    packages=find_packages(),
    install_requires=["httpx>=0.25.0"],
    python_requires=">=3.9",
    license="Apache-2.0",
)
