from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Tuple
from selenium.webdriver.common.by import By

PAGE_TITLE = (By.XPATH, "//span[@class='title']")


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: Tuple, time=10) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}"
                                                      )

    def find_elements(self, locator: Tuple, time=10) -> List:
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def find_button(self, locator: Tuple, time=10) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def should_be_right_title(self, title):
        page_title = self.find_element(PAGE_TITLE).text
        return page_title == title
