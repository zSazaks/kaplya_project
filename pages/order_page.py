import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Order_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://kaplya39.ru/order/"

    # Test data
    fio = "Иванов Иван Иванович"
    email = "test@test.ru"
    tel = "9999999991"
    address = "Адрес"

    # Locators
    further_button = "//a[contains(text(), 'Далее')]"
    fio_field = "//input[@id='soa-property-1']"
    email_field = "//input[@id='soa-property-2']"
    tel_field = "(//input[@id='soa-property-3'])[2]"
    address_field = "//textarea[@id='soa-property-7']"
    order_item_name = "//div[@class='bx-soa-item-title']"


    # Getters
    def get_further_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.further_button)))

    def get_fio_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.fio_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_tel_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.tel_field)))

    def get_address_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.address_field)))

    def get_order_item_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.order_item_name)))

    # Actions
    def click_further_button(self):
        self.get_further_button().click()

    def input_fio_field(self, fio):
        self.get_fio_field().send_keys(fio)

    def input_email_field(self, email):
        self.get_email_field().send_keys(email)
        self.get_email_field().send_keys(Keys.TAB)

    def input_tel_field(self, tel):
        self.get_tel_field().send_keys(tel)

    def input_address_field(self, address):
        self.get_address_field().send_keys(address)

    """Проверка выбранного фильтра"""
    def assert_item_name(self):
        text = self.get_order_item_name().text
        assert text == "Аквафор Автомат питьевой воды Морион DWM-101S, арт.и8471"
        print(text)
        print("Выбран корркетный фильтр!")


    # Methods
    """Заполнение информации для оформления заказа и завершение оформления"""
    def checkout_order(self):
        self.get_current_url()
        self.driver.get(self.url)
        self.click_further_button()
        self.click_further_button()
        time.sleep(4)
        self.click_further_button()
        self.input_fio_field(self.fio)
        self.input_email_field(self.email)
        self.input_tel_field(self.tel)
        self.input_address_field(self.address)
        self.click_further_button()
        self.assert_item_name()