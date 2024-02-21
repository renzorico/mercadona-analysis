from selenium.webdriver.chrome.options import Options

def get_webdriver_options():
    opts = Options()
    opts.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    )
    opts.add_argument("--headless")
    return opts
