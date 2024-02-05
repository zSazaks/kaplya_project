from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Systems_reverse_osmos_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://kaplya39.ru/catalog/filtry_dlya_vody/kukhonnye_filtry/sistemy_obratnogo_osmosa/"

    # Test data
    min_price = "14000"
    max_price = "15000"

    # Locators
    aquaphor_checkbox = "//span[@title='Аквафор']"
    hit_checkbox = "//span[@title='Хит']"
    show_button = "//input[@id='set_filter']"
    min_price_field = "//input[@class='min-price']"
    max_price_field = "//input[@class='max-price']"
    result_filter_popup = "//div[@id='modef']"
    in_basket_button = "//span[contains(text(), 'В корзину')]"
    go_to_basket_button = "//span[contains(text(), 'Перейти в корзину')]"
    catalog_item = "//div[@class='catalog_item main_item_wrapper item_wrap ']"


    # Getters
    def get_aquaphor_checkbox(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.aquaphor_checkbox)))

    def get_hit_checkbox(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.hit_checkbox)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.show_button)))

    def get_min_price_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.min_price_field)))

    def get_max_price_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.max_price_field)))

    def get_result_filter_popup(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.result_filter_popup)))

    def get_in_basket_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.in_basket_button)))

    def get_go_to_basket_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.go_to_basket_button)))

    def get_catalog_item(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.catalog_item)))

    # Actions
    def click_aquaphor_checkbox(self):
        self.get_aquaphor_checkbox().click()

    def click_hit_checkbox(self):
        self.get_hit_checkbox().click()

    def click_show_button(self):
        self.get_result_filter_popup()
        self.get_show_button().click()

    def input_max_price_filed(self, max_price_field):
        self.get_max_price_field().send_keys(max_price_field)

    def input_min_price_field(self, min_price_field):
        self.get_min_price_field().send_keys(min_price_field)

    def click_in_basket_button(self):
        self.get_in_basket_button().click()

    def click_go_to_basket_button(self):
        self.get_go_to_basket_button().click()

    def move_to_catalog_item(self, driver):
        ActionChains(driver).move_to_element(self.get_catalog_item()).perform()

    # Methods
    """Выбор фильтра аквафор от 14 до 15 тыс рублей и добавление его в корзину"""
    def select_aquaphor_hit_from_fourten_before_fifteen_thosand_filter(self):
        self.get_current_url()
        self.driver.get(self.url)
        self.click_aquaphor_checkbox()
        self.click_hit_checkbox()
        self.input_min_price_field(self.min_price)
        self.input_max_price_filed(self.max_price)
        self.click_show_button()
        self.move_to_catalog_item(self.driver)
        self.click_in_basket_button()
        self.click_go_to_basket_button()
        self.assert_url("https://kaplya39.ru/basket/")