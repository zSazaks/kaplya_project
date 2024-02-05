from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Basket_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://kaplya39.ru/basket/"

    # Locators
    checkout_button = "//button[@data-entity='basket-checkout-button']"


    # Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()


    # Methods

    """Прехеход к оформлению заказа из корзины"""
    def checkout(self):
        self.get_current_url()
        self.driver.get(self.url)
        self.click_checkout_button()
        self.assert_url("https://kaplya39.ru/order/")