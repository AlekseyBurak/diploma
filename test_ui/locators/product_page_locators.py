from selenium.webdriver.common.by import By

SHOPPING_CART = (By.XPATH, "//a[@class='shopping_cart_link']")

BURGER_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
LOGOUT_BUTTON = (By.XPATH, "//a[@id='logout_sidebar_link']")
PRODUCT_SORT = (By.XPATH, "//select[@class='product_sort_container']")


PRICE_FROM_PRODUCTS_PAGE = (By.XPATH, "//div[@class='inventory_item_price']")
PRODUCT_TITLE_FROM_PRODUCTS_PAGE = (By.XPATH, "//div[@class='inventory_item_name']")
ADD_TO_CART_BUTTON_FROM_PRODUCTS_PAGE = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")
PRODUCT_FROM_LIST = (By.XPATH, "//div[@class='inventory_item_name']")
