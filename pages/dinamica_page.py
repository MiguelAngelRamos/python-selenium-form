from selenium.webdriver.common.by import By
from .base_page import BasePage


class DinamicaPage(BasePage):
    # Localizadores
    BTN_ALERTA = (By.ID, "btn-alerta")
    BTN_DELAY = (By.ID, "btn-mostrar-delay")
    MSG_OCULTO = (By.ID, "mensaje-oculto")
    LINK_GOOGLE = (By.ID, "link-google")

    def trigger_alert(self) -> None:
        """Dispara la alerta del botón."""
        self.safe_click(self.BTN_ALERTA)

    def trigger_delay(self) -> None:
        """Hace click en el botón que luego muestra el mensaje con retardo."""
        self.safe_click(self.BTN_DELAY)

    def delayed_message_text(self) -> str:
        """Devuelve el texto del mensaje que aparece tras el delay."""
        elem = self.wait_visible(self.MSG_OCULTO)
        return elem.text

    def click_external_link(self) -> None:
        """Abre el link externo (target=_blank)."""
        self.safe_click(self.LINK_GOOGLE)
