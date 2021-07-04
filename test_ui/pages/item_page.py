from test_ui.base_page import BasePage
from test_ui.locators import item_page_locators


class ItemPage(BasePage):

    def get_product_title_from_item_page(self):
        title = self.find_element(item_page_locators.PRODUCT_TITLE_FROM_ITEM_PAGE).text
        return title

    def get_product_price_from_item_page(self):
        price = self.find_element(item_page_locators.PRODUCT_PRICE_FROM_ITEM_PAGE).text
        return price

    def add_product_to_cart_from_item_page(self):
        self.find_element(item_page_locators.ADD_TO_CART_BUTTON).click()

    def go_to_cart(self):
        self.find_element(item_page_locators.SHOPPING_CART).click()
