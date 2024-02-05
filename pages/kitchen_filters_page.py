from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Kitchen_filters_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://kaplya39.ru/catalog/filtry_dlya_vody/kukhonnye_filtry/"

    # Locators
    systems_reverse_osmos_link = "(//a[@href='/catalog/filtry_dlya_vody/kukhonnye_filtry/sistemy_obratnogo_osmosa/'])[1]"

    # Getters
    def get_systems_reverse_osmos_link(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.systems_reverse_osmos_link)))

    # Actions
    def click_systems_reverse_osmos_link(self):
        self.get_systems_reverse_osmos_link().click()

    # Methods
    """Переход в системы обратного осмоса"""
    def go_to_systems_reverse_osmos(self):
        self.get_current_url()
        self.driver.get(self.url)
        self.click_systems_reverse_osmos_link()
        self.assert_url("https://kaplya39.ru/catalog/filtry_dlya_vody/kukhonnye_filtry/sistemy_obratnogo_osmosa/")