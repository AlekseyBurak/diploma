from test_ui.base_page import BasePage
from test_ui.locators import product_page_locators
from selenium.webdriver.support.ui import Select


class ProductPage(BasePage):

    def get_product_title_from_product_page(self, ind: int):
        product_title_list = self.find_elements(product_page_locators.PRODUCT_TITLE_FROM_PRODUCTS_PAGE)
        return product_title_list[ind].text

    def get_product_price_from_product_page(self, ind: int):
        product_price_list = self.find_elements(product_page_locators.PRICE_FROM_PRODUCTS_PAGE)
        return product_price_list[ind].text

    def go_to_product_page_from_product_s_page(self):
        self.find_element(product_page_locators.PRODUCT_TITLE_FROM_PRODUCTS_PAGE).click()

    def add_product_to_cart_from_products_page(self, ind: int):
        buttons_list = self.find_elements(product_page_locators.ADD_TO_CART_BUTTON_FROM_PRODUCTS_PAGE)
        buttons_list[ind].click()

    def go_to_cart(self):
        self.find_element(product_page_locators.SHOPPING_CART).click()

    def go_to_first_item_s_page(self):
        self.find_element(product_page_locators.PRODUCT_FROM_LIST).click()

    def roll_burger_menu(self):
        self.find_element(product_page_locators.BURGER_MENU).click()

    def choose_logout_button(self):
        self.find_button(product_page_locators.LOGOUT_BUTTON).click()

    def get_list_of_products_titles(self):
        list_of_products = self.find_elements(product_page_locators.PRODUCT_TITLE_FROM_PRODUCTS_PAGE)
        list_of_titles = []
        for i in list_of_products:
            list_of_titles.append(i.text)
        return list_of_titles

    def select_sort_by_price_from_low(self):
        select = Select(self.find_element(product_page_locators.PRODUCT_SORT))
        select.select_by_value("lohi")

    def select_sort_by_price_from_high(self):
        select = Select(self.find_element(product_page_locators.PRODUCT_SORT))
        select.select_by_value("hilo")

    def should_be_correct_sorting(self, list1, list2):
        return list1[0] == list2[-1]
