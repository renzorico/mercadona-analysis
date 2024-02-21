from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random


def get_valid_product_ids(start=1000, end=100001, chunk_size=1):
    valid_ids = []
    opts = Options()
    opts.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    )
    opts.add_argument("--headless")
    driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=opts)

    try:
        for number in range(start, end, chunk_size):
            for i in range(chunk_size):
                product_number = number + i
                url = f'https://tienda.mercadona.es/product/{product_number}'
                driver.get(url)
                try:
                    WebDriverWait(driver, 1).until( EC.presence_of_element_located((By.XPATH, '//h1[@class="title2-r public-product-detail__description"]')))
                    valid_ids.append(product_number)
                    sleep(random.uniform(0.5, 1.5))
                except Exception as e:
                    pass
    finally:
        driver.quit()
    return valid_ids

if __name__ == '__main__':
    get_valid_product_ids()
