from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout:int =10):
        self.driver=driver
        self.wait=WebDriverWait(driver, timeout)
    
    def open(self, url: str):
        self.driver.get(url)
    
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))