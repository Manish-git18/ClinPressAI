"""
CLI entry point for the Pharma Press Analyzer.
"""
import os
from .analyzer import PharmaPressReleaseAnalyzer

def main():
    serp_key = os.getenv('SERP_API_KEY', '')
    gemini_key = os.getenv('GEMINI_API_KEY', '')
    analyzer = PharmaPressReleaseAnalyzer(serp_key, gemini_key)
    analyzer.run()

if __name__ == '__main__':
    main()
