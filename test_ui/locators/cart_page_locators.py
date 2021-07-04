from selenium.webdriver.common.by import By

PRODUCT_TITLE = (By.XPATH, "//div[@class='inventory_item_name']")
PRODUCT_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")

PRODUCT = (By.XPATH, "//div[@class='cart_item']")

CHECKOUT_BUTTON = (By.XPATH, "//button[@id='checkout']")

FINISH_BUTTON = (By.XPATH, "//button[@class='btn btn_action btn_medium cart_button']")

REMOVE_BUTTON = (By.XPATH, "//button[@class='btn btn_secondary btn_small cart_button']")

SUCCESSFUL_ORDER = (By.XPATH, "//h2[@class='complete-header']")

CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[@id='continue-shopping']")

# CHECKOUT

CHECKOUT_FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
CHECKOUT_LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
CHECKOUT_ZIP = (By.XPATH, "//input[@placeholder='Zip/Postal Code']")
CHECKOUT_SUBMIT = (By.XPATH, "//input[@type='submit']")
