from .base_page import BasePage
from selenium.webdriver.common.by import By

class DinamicaPage(BasePage):
    # Localizadores | btn-alerta | btn-mostrar-delay | mensaje-oculto | link-google

    BTN_ALERTA = (By.ID, "btn-alerta")
    BTN_DELAY = (By.ID, "btn-mostrar-delay")
    MSG_OCULTO = (By.ID, "mensaje-oculto")
    LINK_GOOGLE = (By.ID, "link-google" )

    ## Trigger
    def trigger_alert(self):
        self.wait_present(self.BTN_ALERTA).click()
    
    def trigger_delay(self):
        self.wait_present(self.BTN_DELAY).click()

    
    def delayed_message_text(self) -> str:
        element = self.wait_visible(self.MSG_OCULTO)
        return element.text
    
    def click_external_link(self):
        self.wait_present(self.LINK_GOOGLE).click()
    


