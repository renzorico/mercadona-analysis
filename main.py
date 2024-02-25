from utils.scraper import MercadonaScraper
from utils.categories_extractor import get_valid_category_numbers
from utils.driver import get_headless_driver
import pandas as pd
from datetime import datetime

def process_price(price):
    return float(price.split()[0].replace(',', '.'))

def process_unidad(unidad):
    return unidad.replace('/', '')

def save_to_csv(data, file_name):
    df = pd.DataFrame([vars(product) for product in data])
    df['price'] = df['price'].apply(process_price)
    df['unit'] = df['unit'].apply(process_unidad)
    df.to_csv(f'data/{file_name}')

def main():
    driver = get_headless_driver()
    mercadona_scraper = MercadonaScraper(driver)
    category_numbers = get_valid_category_numbers()
    data = []

    for category_number in category_numbers:
        products = mercadona_scraper.scrape_category(category_number)
        data.extend(products)

    current_date = datetime.now()
    formatted_date = current_date.strftime("%d%m%y")
    file_name = f"mercadona_products_{formatted_date}.csv"

    save_to_csv(data, file_name)

    driver.quit()

if __name__ == "__main__":
    main()
