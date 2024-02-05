from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.main_page import Main_page
from pages.catalog_page import Catalog_page
from pages.kitchen_filters_page import Kitchen_filters_page
from pages.systems_reverse_osmos_page import Systems_reverse_osmos_page
from pages.basket_page import Basket_page
from pages.order_page import Order_page


"""Покупка кухонного фильтра обратного осмоса"""
def test_buy_kitchen_filter_osmos():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test")

    mp = Main_page(driver)
    mp.go_to_catalog()

    cp = Catalog_page(driver)
    cp.go_to_kitchen_filters()

    kfp = Kitchen_filters_page(driver)
    kfp.go_to_systems_reverse_osmos()

    srop = Systems_reverse_osmos_page(driver)
    srop.select_aquaphor_hit_from_fourten_before_fifteen_thosand_filter()

    bp = Basket_page(driver)
    bp.checkout()

    op = Order_page(driver)
    op.checkout_order()

    driver.quit()

    print("Finish Test")