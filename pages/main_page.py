from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://kaplya39.ru/"

    # Locators
    catalog_dropdown = "(//a[@class='dropdown-toggle'])[1]"

    # Getters
    def get_catalog_dropdown(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.catalog_dropdown)))

    # Actions
    def click_catalog_dropdown(self):
        self.get_catalog_dropdown().click()

    # Methods
    """Переход в каталог"""
    def go_to_catalog(self):
        self.get_current_url()
        self.driver.get(self.url)
        self.click_catalog_dropdown()
        self.assert_url("https://kaplya39.ru/catalog/")