from setuptools import setup, find_packages

setup(
    name="pharma-pr-scraper-analyzer",
    version="0.1.0",
    description="Analyze pharmaceutical press releases for clinical trial information",
    author="Your Name",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "beautifulsoup4>=4.12",
        "google-generativeai>=0.1.0",
        "google-search-results>=2.4.0",
        "pandas>=1.5.0",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "pharma-analyze=pharma_pr_scraper_analyzer.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
