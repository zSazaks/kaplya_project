from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Catalog_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://kaplya39.ru/catalog/"

    # Locators
    kitchen_filters_link = "(//a[@class='dark_link'])[2]"

    # Getters
    def get_kitchen_filters_link(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.kitchen_filters_link)))

    # Actions
    def click_kitchen_filters_link(self):
        self.get_kitchen_filters_link().click()

    # Methods
    """Переход в раздел с кухонными фильтрами"""
    def go_to_kitchen_filters(self):
        self.get_current_url()
        self.driver.get(self.url)
        self.click_kitchen_filters_link()
        self.assert_url("https://kaplya39.ru/catalog/filtry_dlya_vody/kukhonnye_filtry/")