from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from utils.scraper import MercadonaScraper
from utils.categories_extractor import get_valid_category_numbers
import pandas as pd
from time import sleep
from datetime import datetime

def main():
    opts = Options()
    opts.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    )
    opts.add_argument("--headless")
    driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=opts)

    mercadona_scraper = MercadonaScraper(driver)

    category_numbers = get_valid_category_numbers()

    data = []
    for category_number in category_numbers:
        products = mercadona_scraper.scrape_category(category_number)
        data.extend(products)

    df = pd.DataFrame([vars(product) for product in data])
    def process_price(price):
        return float(price.split()[0].replace(',', '.'))

    df['price'] = df['price'].apply(process_price)

    def process_unidad(unidad):
        return unidad.replace('/', '')

    df['unit'] = df['unit'].apply(process_unidad)

    current_date = datetime.now()
    formatted_date = current_date.strftime("%d%m%y")
    file_name = f"mercadona_products_{formatted_date}.csv"
    df.to_csv(f'data/{file_name}')

    driver.quit()
    sleep(3)

if __name__ == "__main__":
    main()
