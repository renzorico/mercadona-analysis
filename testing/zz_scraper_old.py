from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
)
opts.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=opts
)

numbers = [27, 28, 29, 31, 32, 34, 36, 37, 38, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 58, 59, 60, 62, 64, 65, 66, 68, 69, 71, 72, 75, 77, 78, 79, 80, 81, 83, 84, 86, 88, 89, 90, 92, 95, 97, 98, 99, 100, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 115, 116, 117, 118, 120, 121, 122, 123, 126, 127, 129, 130, 132, 133, 135, 138, 140, 142, 143, 145, 147, 148, 149, 150, 151, 152, 154, 155, 156, 158, 159, 161, 162, 163, 164, 166, 168, 169, 170, 171, 173, 174, 181, 185, 186, 187, 188, 189, 190, 191, 192, 194, 196, 198, 199, 201, 202, 203, 206, 207, 208, 210, 212, 213, 214, 216, 217, 218, 219, 221, 222, 225, 226, 229, 230, 231, 232, 233, 234, 235, 237, 238, 239, 241, 243, 244, 789, 884, 897]

data = []
for number in numbers:
    url = f"https://tienda.mercadona.es/categories/{number}"
    driver.get(url)

    try:
        category_name_element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, '//h1[@class="category-detail__title title1-b"]')) )

        category_name = category_name_element.text

        name_products = driver.find_elements( By.XPATH, '//h4[@class="subhead1-r product-cell__description-name"]' )
        format_products = driver.find_elements( By.XPATH, '//div[@class="product-format product-format__size--cell"]' )
        price_products = driver.find_elements( By.XPATH, '//p[@class="product-price__unit-price subhead1-b"]' )
        price_products_format = driver.find_elements( By.XPATH, '//p[@class="product-price__extra-price subhead1-r"]' )

        for (name, name_product, format_product, price_product, price_product_format) in zip(
            name_products,
            name_products,
            format_products,
            price_products,
            price_products_format):
            info_product = {
                "Categoria": category_name,
                "Nombre": name_product.text,
                "Formato": format_product.text,
                "Precio": price_product.text,
                "Unidad": price_product_format.text,
            }
            data.append(info_product)
    except Exception as e:
        print(f"Error processing category {number}: {str(e)}")

df = pd.DataFrame(data)
df.to_csv('data/mercadona_products.csv')
sleep(3)

# categories = driver.find_elements(By.XPATH, '//label[@class="subhead1-r"]')

# product_names = driver.find_elements(
#     By.XPATH, '//h4[@data-test="product-cell-name"]'
# )
# product_formats = driver.find_elements(
#     By.XPATH, '//div[@class="product-format product-format__size--cell"]'
# )
# product_prices = driver.find_elements(By.XPATH, '//div[@class="product-price"]')

#     for category, category, product_name, product_format, product_price in zip(
#         categories, subcategories, product_names, product_formats, product_prices
#     ):
#         product_info = {
#             "Category": category.text,
#             "category": category.text,
#             "Product Name": product_name.text,
#             "Product Format": product_format.text,
#             "Product Price": product_price.text,
#         }
#         data.append(product_info)

# df = pd.DataFrame(data)


# class Product:
#     def __init__(self,title,formatting,price,link):
#         self.title = title
#         self.formatting = formatting
#         self.price = price
#         self.link = link

# class MercadonaScraper:
#     login_url = "https://tienda.mercadona.es/categories/112"
#     zip_code = "08014"

#     def __init__(self):
#         service = Service(ChromeDriverManager(version="114.0.5735.90").install())
#         driver = webdriver.Chrome(service=service)
#         self.driver = webdriver.Chrome("bin/chromedriver")
#         self.login()

#     def login(self):
#         self.driver.get(self.login_url)
#         zip_code_popup_input = self.driver.find_element_by_css_selector(
#             "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > div > input"
#         )
#         zip_code_popup_input.send_keys(self.zip_code)
#         continue_button = self.driver.find_element_by_css_selector(
#             "#root > div.ui-focus-trap > div > div:nth-child(2) > div > form > button"
#         )

#         continue_button.click()

#     def scrape(self):
#         pass

#     def close(self):
#         self.driver.quit()


# if __name__ == "__main__":
#     scraper = MercadonaScraper()
#     scraper.scrape()
#     scraper.close()
