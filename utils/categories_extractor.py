from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def get_valid_category_numbers():
    category_numbers = []

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    for start_num in range(1, 1001, 200):
        end_num = min(start_num + 199, 1000)  # Adjust as needed

        for num in range(start_num, end_num + 1):
            url = f"https://tienda.mercadona.es/categories/{num}"
            driver.get(url)

            try:
                # Attempt to find elements on the page
                categories = driver.find_elements(By.XPATH, '//label[@class="subhead1-r"]')
                subcategories = driver.find_elements(By.XPATH, '//button[@class="category-item__link"]')

                # If elements are found, consider the URL valid
                if categories or subcategories:
                    category_numbers.append(num)
            except Exception as e:
                # If an exception occurs, the URL is invalid or doesn't contain expected elements
                print(f"Invalid URL: {url}, Error: {str(e)}")

        driver.quit()
        options.add_argument("--headless")  # Re-add this line
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.quit()
    return category_numbers
