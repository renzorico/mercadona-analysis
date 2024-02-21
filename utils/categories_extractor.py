from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def get_valid_category_numbers():
    category_numbers = []

    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

    # for start_num in range(1, 1001, 200):
    #     end_num = min(start_num + 199, 1000)
    # Just for testing purposes
    for start_num in range(1, 50, 10):
        end_num = min(start_num + 10, 50)

        for num in range(start_num, end_num + 1):
            url = f"https://tienda.mercadona.es/categories/{num}"
            driver.get(url)

            try:
                categories = driver.find_elements(By.XPATH, '//label[@class="subhead1-r"]')
                subcategories = driver.find_elements(By.XPATH, '//button[@class="category-item__link"]')

                if categories or subcategories:
                    category_numbers.append(num)
            except Exception as e:
                print(f"Invalid URL: {url}, Error: {str(e)}")

        driver.quit()
        opts.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

    driver.quit()
    return category_numbers
