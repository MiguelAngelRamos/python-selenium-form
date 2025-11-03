from pages.dinamica_page import DinamicaPage
from selenium.webdriver.common.alert import Alert
import pytest


@pytest.mark.dinamica
def test_alert_y_mensaje_con_retrasdo(driver, base_url):
    page = DinamicaPage(driver)
    page.open(f"{base_url}/index.html")
    page.trigger_alert()
    alert = Alert(driver)
    assert "alerta" in alert.text.lower()
    alert.accept()
