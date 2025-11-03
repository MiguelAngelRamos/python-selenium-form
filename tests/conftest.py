import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://web-form-selenium.netlify.app/")

@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    # Usar solo para depuración local ( options.add_experimental_option("detach", True))
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def reset_between_test(driver, base_url):
    driver.delete_all_cookies()
    driver.get(f"{base_url}/index.html")
    yield