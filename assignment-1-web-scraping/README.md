# Web Scraping Assignment

A Python web scraping project developed as part of the Build Fellowship's AI-Powered Text Generation Portal.

## Overview

- Scrapes country information from [Scrape This Site](https://www.scrapethissite.com/pages/simple/) using Requests and BeautifulSoup.
- Extracts the name, capital, population, and area of 250 countries.
- Saves the extracted data into `countries.csv`.

## Technologies

Python, Requests, BeautifulSoup, Selenium, uv

## How to Run

Install dependencies:

`uv sync`

Run the country scraper:

`uv run main.py`

## Output

`countries.csv` — Contains 250 country records with four columns: Name, Capital, Population, and Area.