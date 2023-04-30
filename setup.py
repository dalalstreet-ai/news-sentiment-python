from setuptools import setup, find_packages

setup(
    name="dalalstreet-news-sentiment",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    python_requires=">=3.6",
    author="Dalalstreet.ai",
    author_email="connect@dalalstreet.ai",
    description="A Python SDK for fetching news sentiment data as positive, negative and neutral sentiment scores for a given stock.",
    url="https://github.com/dalalstreet-ai/news-sentiment-python",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
