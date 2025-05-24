# Pharma PR Scraper and Analyzer

A Python tool to discover, extract, and analyze pharmaceutical press releases for clinical trial information (NCT IDs) using SerpAPI and Google Gemini.

## Features
- Search press releases via SerpAPI (or fallback URLs)
- Scrape and extract text content
- Analyze with Google Gemini to extract trial metadata
- Output results as CSV

## Installation

```bash
git clone https://github.com/Manish-git18/pharma-press-release-analyzer.git
cd pharma-press-release-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
export SERP_API_KEY=your_serpapi_key
export GEMINI_API_KEY=your_gemini_key
python -m pharma_pr_scraper_analyzer
```

## Development

- Lint with `flake8` and `black`
- Run tests: `pytest`

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
