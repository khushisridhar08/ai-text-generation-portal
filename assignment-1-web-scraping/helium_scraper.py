
import csv
from helium import start_chrome, get_driver, kill_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://quotes.toscrape.com/js/"

start_chrome(url)
driver = get_driver()

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "quote"))
    )

    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    print("Total quotes found:", len(quotes))

    with open("quotes_helium.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])

        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text

            tags = quote.find_elements(By.CLASS_NAME, "tag")
            tag_names = [tag.text for tag in tags]

            writer.writerow([text, author, ", ".join(tag_names)])

    print("Quotes successfully saved to quotes_helium.csv")

finally:
    kill_browser()
