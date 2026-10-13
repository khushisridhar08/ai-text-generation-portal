# Assignment 1 - Web Scraping

This assignment is part of the AI Text Generation Portal project under the Build Fellowship. The goal was to get familiar with web scraping using Python and explore scraping both static and JavaScript-rendered websites.

## Web Scraping with BeautifulSoup

Used Requests and BeautifulSoup to scrape country information from [Scrape This Site](https://www.scrapethissite.com/pages/simple/). Extracted the name, capital, population, and area of 250 countries and saved the data to `countries.csv`.

## Scraping Dynamic Websites

Explored Selenium and Helium to scrape JavaScript-rendered content from [Quotes to Scrape](https://quotes.toscrape.com/js/). Extracted quotes, authors, and tags, and saved the results to `quotes_selenium.csv` and `quotes_helium.csv`.

## Running the Scripts

Install the dependencies:

`uv sync`

Run the scripts:

```bash
uv run main.py
uv run selenium_scraper.py
uv run helium_scraper.py
```