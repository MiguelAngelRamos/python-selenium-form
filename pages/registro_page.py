from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegistroPage(BasePage):
    # Localizadores 
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    EMAIL = (By.ID, "email")
    BTN_SUBMIT = (By.ID, "submit-registro")
    FEEDBACK = (By.ID, "resultado-registro")

    def fill(self, username: str, password: str, email:str):
        self.wait_present(self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def submit(self):
        self.driver.find_element(*self.BTN_SUBMIT).click()

    def feedback_text(self)-> str:
        return self.wait_present(self.FEEDBACK).text
    
    def has_success_class(self) -> bool:
        classes = self.wait_present(self.FEEDBACK).get_attribute("class")
        return "mensaje-exito" in classes.split()
    
    def has_error_class(self) -> bool:
        classes = self.wait_present(self.FEEDBACK).get_attribute("class")
        return "mensaje-error" in classes.split()

        
