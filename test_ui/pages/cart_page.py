from selenium.common.exceptions import TimeoutException

from test_ui.base_page import BasePage
from test_ui.locators import cart_page_locators
import pytest


class CartPage(BasePage):

    def get_product_title_from_cart_page(self):
        product_title = self.find_element(cart_page_locators.PRODUCT_TITLE).text
        return product_title

    def get_product_price_from_cart_page(self):
        product_price = self.find_element(cart_page_locators.PRODUCT_PRICE).text
        return product_price

    def remove_product_from_cart(self):
        self.find_element(cart_page_locators.REMOVE_BUTTON).click()

    def continue_shopping_button(self):
        self.find_element(cart_page_locators.CONTINUE_SHOPPING_BUTTON).click()

    def should_be_empty_cart(self):
        try:
            self.find_element(cart_page_locators.PRODUCT, time=5)
            return False
        except TimeoutException:
            return True

    # CHECKOUT
    def click_checkout_button(self):
        self.find_element(cart_page_locators.CHECKOUT_BUTTON).click()

    def send_first_name_checkout_field(self):
        self.find_element(cart_page_locators.CHECKOUT_FIRST_NAME).send_keys('first name')

    def send_last_name_checkout_field(self):
        self.find_element(cart_page_locators.CHECKOUT_LAST_NAME).send_keys('last name')

    def send_zip_checkout_field(self):
        self.find_element(cart_page_locators.CHECKOUT_ZIP).send_keys('zip-zip')

    def submit_checkout(self):
        self.find_element(cart_page_locators.CHECKOUT_SUBMIT).click()

    def click_finish_button_cart(self):
        self.find_element(cart_page_locators.FINISH_BUTTON).click()

    def should_be_successful_order(self):
        header = self.find_element(cart_page_locators.SUCCESSFUL_ORDER).text
        return header == 'THANK YOU FOR YOUR ORDER'
