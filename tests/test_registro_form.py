import pytest
from pages.registro_page import RegistroPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_registro_exito(driver, base_url):
    page = RegistroPage(driver)
    page.open(f"{base_url}/index.html")
    page.fill(username="sofia", password="academyselenium123", email="sofia@selenium.com")
    page.submit()
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "resultado-registro"), "Registro"))
    assert page.has_success_class()
    assert "exitoso" in page.feedback_text().lower()
