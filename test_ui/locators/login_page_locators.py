from selenium.webdriver.common.by import By

LOGIN_PAGE_URL = "https://www.saucedemo.com/"

INPUT_USER_NAME_FIELD = (By.XPATH, "//input[@id='user-name']")
INPUT_PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
