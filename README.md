# 🧠 ClinPressAI

**ClinPressAI** is an AI-powered tool that automates the extraction and structuring of pharmaceutical press releases related to clinical trials. It uses **SerpAPI** to dynamically find recent trial announcements, scrapes full text from press release pages, and applies **Google Gemini** to convert unstructured content into structured insights.

...

## 🚀 Features

- 🔍 **Dynamic Search**: Uses SerpAPI to query recent clinical trial press releases from pharma investor websites.
- 🧠 **Gemini-Powered Analysis**: Extracts trial IDs, drugs, diseases, indications, endpoints, and results using **Google Gemini Pro**.
- 📄 **Structured Output**: Saves results in clean, analysis-ready CSV format.
- 🎛️ **Interactive Widgets**: Fully interactive UI with model selector, result count slider, and date range dropdown.


...

## 📦 Installation

```bash
pip install google-generativeai serpapi beautifulsoup4 requests pandas ipywidgets
