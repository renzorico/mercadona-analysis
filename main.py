from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from utils.scraper import MercadonaScraper
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

    category_numbers = [27, 28, 29, 31, 32, 34, 36, 37, 38, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 58, 59, 60, 62, 64, 65, 66, 68, 69, 71, 72, 75, 77, 78, 79, 80, 81, 83, 84, 86, 88, 89, 90, 92, 95, 97, 98, 99, 100, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 120, 121, 122, 123, 126, 127, 129, 130, 132, 133, 135, 138, 140, 142, 143, 145, 147, 148, 149, 150, 151, 152, 154, 155, 156, 158, 159, 161, 162, 163, 164, 166, 168, 169, 170, 171, 173, 174, 181, 185, 186, 187, 188, 189, 190, 191, 192, 194, 196, 198, 199, 201, 202, 203, 206, 207, 208, 210, 212, 213, 214, 216, 217, 218, 219, 221, 222, 225, 226, 229, 230, 231, 232, 233, 234, 235, 237, 238, 239, 241, 243, 244, 789, 884, 897]

    data = []
    for category_number in category_numbers:
        products = mercadona_scraper.scrape_category(category_number)
        data.extend(products)

    df = pd.DataFrame([vars(product) for product in data])
    def process_price(price):
        return round(float(price.split()[0].replace(',', '.')),2)

    df['price'] = df['price'].apply(process_price)

    def process_unidad(unidad):
        return unidad.replace('/', '')

    df['unit'] = df['unit'].apply(process_unidad)

    current_date = datetime.now()
    formatted_date = current_date.strftime("%d%m%y_")
    file_name = f"mercadona_products_{formatted_date}.csv"
    df.to_csv(f'data/{file_name}')

    driver.quit()
    sleep(3)

if __name__ == "__main__":
    main()
