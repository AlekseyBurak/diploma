from selenium.webdriver.common.by import By

PRODUCT_TITLE_FROM_ITEM_PAGE = (By.XPATH, "//div[@class='inventory_details_name large_size']")
PRODUCT_PRICE_FROM_ITEM_PAGE = (By.XPATH, "//div[@class='inventory_details_price']")
ADD_TO_CART_BUTTON = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")
SHOPPING_CART = (By.XPATH, "//a[@class='shopping_cart_link']")