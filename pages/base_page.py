from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)

Locator = Tuple[By, str]


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def wait_visible(self, locator: Locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_present(self, locator: Locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_clickable(self, locator: Locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def safe_click(self, locator: Locator, retries: int = 2, use_js_fallback: bool = True) -> None:
        last_exc = None
        for _ in range(max(1, retries)):
            try:
                elem = self.wait_clickable(locator)
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center', inline:'center'});",
                    elem,
                )
                self.driver.execute_script("window.scrollBy(0, -80);")
                ActionChains(self.driver).move_to_element(elem).pause(0.05).click().perform()
                return
            except (ElementClickInterceptedException, StaleElementReferenceException) as exc:
                last_exc = exc

        if use_js_fallback:
            elem = self.wait_present(locator)
            self.driver.execute_script("arguments[0].click();", elem)
            return

        if last_exc:
            raise last_exc