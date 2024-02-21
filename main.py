from utils.scraper import MercadonaScraper
from utils.categories_extractor import get_valid_category_numbers
from utils.driver import get_headless_driver
import pandas as pd
from time import sleep
from datetime import datetime

def main():
    driver = get_headless_driver()
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
