import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url, timeout=15)

soup = BeautifulSoup(response.text, "html.parser")

countries = soup.find_all("div", class_="country")

print("Total countries found:", len(countries))

with open("countries.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Capital", "Population", "Area"])

    for country in countries:
        name = country.find("h3", class_="country-name").get_text(strip=True)
        capital = country.find("span", class_="country-capital").get_text(strip=True)
        population = country.find("span", class_="country-population").get_text(strip=True)
        area = country.find("span", class_="country-area").get_text(strip=True)

        writer.writerow([name, capital, population, area])

print("Country data successfully saved to countries.csv")