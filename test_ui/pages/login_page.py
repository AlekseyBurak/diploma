
from selenium.common.exceptions import TimeoutException

from test_ui.base_page import BasePage
from test_ui.locators import login_page_locators
ACCEPTED_USER_NAME = 'standard_user'
ACCEPTED_PASSWORD = 'secret_sauce'


class LoginPage(BasePage):
    def go_to_login_page(self):
        self.driver.get(login_page_locators.LOGIN_PAGE_URL)

    def send_user_name(self):
        self.find_element(login_page_locators.INPUT_USER_NAME_FIELD).send_keys(ACCEPTED_USER_NAME)

    def send_password(self):
        self.find_element(login_page_locators.INPUT_PASSWORD_FIELD).send_keys(ACCEPTED_PASSWORD)

    def click_login_button(self):
        self.find_element(login_page_locators.LOGIN_BUTTON).click()

    def should_be_login_page(self):
        try:
            self.find_element(login_page_locators.INPUT_USER_NAME_FIELD, time=2)
            self.find_element(login_page_locators.INPUT_PASSWORD_FIELD, time=2)
            self.find_element(login_page_locators.LOGIN_BUTTON, time=2)
            return True
        except TimeoutException:
            return False
