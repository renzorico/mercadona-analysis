# mercadona_scraper/scraper.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .product import Product

class MercadonaScraper:
    def __init__(self, driver):
        self.driver = driver

    def scrape_category(self, category_number):
        url = f"https://tienda.mercadona.es/categories/{category_number}"
        self.driver.get(url)

        try:
            category_name_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//h1[@class="category-detail__title title1-b"]'))
            )
            category_name = category_name_element.text

            name_elements = self.driver.find_elements(By.XPATH, '//h4[@class="subhead1-r product-cell__description-name"]')
            format_elements = self.driver.find_elements(By.XPATH, '//div[@class="product-format product-format__size--cell"]')
            price_elements = self.driver.find_elements(By.XPATH, '//p[@class="product-price__unit-price subhead1-b"]')
            price_format_elements = self.driver.find_elements(By.XPATH, '//p[@class="product-price__extra-price subhead1-r"]')

            products = []
            for name, format, price, price_format in zip(name_elements, format_elements, price_elements, price_format_elements):
                product = Product(category_name, name.text, format.text, price.text, price_format.text)
                products.append(product)

            return products

        except Exception as e:
            print(f"Error processing category {category_number}: {str(e)}")
            return []
