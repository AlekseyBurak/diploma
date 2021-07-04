import allure
from test_ui.pages.login_page import LoginPage
from test_ui.pages.product_page import ProductPage
from test_ui.pages.cart_page import CartPage
from test_ui.pages.item_page import ItemPage


CART_TITLE = "YOUR CART"
PRODUCTS_TITLE = "PRODUCTS"
CHECKOUT_TITLE = "CHECKOUT: YOUR INFORMATION"
IND = 0


class TestSwagLabs:
    @allure.story('Login')
    def test_login_swag(self, driver):
        with allure.step('Login'):
            login_page = LoginPage(driver)
            login_page.go_to_login_page()
            login_page.send_user_name()
            login_page.send_password()
            login_page.click_login_button()
            product_page = ProductPage(driver)
            assert product_page.should_be_right_title(PRODUCTS_TITLE)

    @allure.story('Login-Logout')
    def test_logoff_swag(self, driver):
        with allure.step('Login'):
            login_page = LoginPage(driver)
            login_page.go_to_login_page()
            login_page.send_user_name()
            login_page.send_password()
            login_page.click_login_button()
            product_page = ProductPage(driver)
            assert product_page.should_be_right_title(PRODUCTS_TITLE)
        with allure.step('Logout'):
            product_page.roll_burger_menu()
            product_page.choose_logout_button()
            assert login_page.should_be_login_page()

    @allure.story('Add product from catalog page')
    def test_add_product_from_product_s_page_to_cart(self, driver):
        with allure.step('Login'):
            login_page = LoginPage(driver)
            login_page.go_to_login_page()
            login_page.send_user_name()
            login_page.send_password()
            login_page.click_login_button()
            product_page = ProductPage(driver)
            assert product_page.should_be_right_title(PRODUCTS_TITLE)
        with allure.step('Add item to cart. Get title and price'):
            product_title_product_page = product_page.get_product_title_from_product_page(IND)
            product_price_product_page = product_page.get_product_price_from_product_page(IND)
            product_page.add_product_to_cart_from_products_page(IND)
            product_page.go_to_cart()
            cart_page = CartPage(driver)
            assert cart_page.should_be_right_title(CART_TITLE)
        with allure.step('Check item in cart'):
            product_title_cart_page = cart_page.get_product_title_from_cart_page()
            product_price_cart_page = cart_page.get_product_price_from_cart_page()
            assert product_title_product_page == product_title_cart_page
            assert product_price_product_page == product_price_cart_page
        with allure.step('Checkout'):
            cart_page.click_checkout_button()
            assert cart_page.should_be_right_title(CHECKOUT_TITLE)
            cart_page.send_first_name_checkout_field()
            cart_page.send_last_name_checkout_field()
            cart_page.send_zip_checkout_field()
            cart_page.submit_checkout()
            cart_page.click_finish_button_cart()
            assert cart_page.should_be_successful_order()

    @allure.story('Add product from prod page')
    def test_add_product_from_product_page_to_cart(self, driver):
        with allure.step('Login'):
            login_page = LoginPage(driver)
            login_page.go_to_login_page()
            login_page.send_user_name()
            login_page.send_password()
            login_page.click_login_button()
            product_s_page = ProductPage(driver)
            assert product_s_page.should_be_right_title(PRODUCTS_TITLE)
        with allure.step('Go to prod page'):
            product_s_page.go_to_product_page_from_product_s_page()
            item_page = ItemPage(driver)
        with allure.step('Get title and price'):
            product_title_item_page = item_page.get_product_title_from_item_page()
            product_price_item_page = item_page.get_product_price_from_item_page()
            item_page.add_product_to_cart_from_item_page()
            item_page.go_to_cart()
        with allure.step('Check item in cart'):
            cart_page = CartPage(driver)
            assert cart_page.should_be_right_title(CART_TITLE)
            product_title_cart_page = cart_page.get_product_title_from_cart_page()
            product_price_cart_page = cart_page.get_product_price_from_cart_page()
            assert product_title_item_page == product_title_cart_page
            assert product_price_item_page == product_price_cart_page
        with allure.step('Checkout'):
            cart_page.click_checkout_button()
            assert cart_page.should_be_right_title(CHECKOUT_TITLE)
            cart_page.send_first_name_checkout_field()
            cart_page.send_last_name_checkout_field()
            cart_page.send_zip_checkout_field()
            cart_page.submit_checkout()
            cart_page.click_finish_button_cart()
            assert cart_page.should_be_successful_order()

    @allure.story('Remove product from cart')
    def test_remove_product_from_cart(self, driver):
        with allure.step('Login'):
            login_page = LoginPage(driver)
            login_page.go_to_login_page()
            login_page.send_user_name()
            login_page.send_password()
            login_page.click_login_button()
        with allure.step('Add to cart'):
            product_page = ProductPage(driver)
            assert product_page.should_be_right_title(PRODUCTS_TITLE)
            product_page.add_product_to_cart_from_products_page(IND)
        with allure.step('Check item in cart'):
            product_page.go_to_cart()
            cart_page = CartPage(driver)
            assert cart_page.should_be_right_title(CART_TITLE)
        with allure.step('Remove item'):
            cart_page.remove_product_from_cart()
            assert cart_page.should_be_empty_cart()

    @allure.story('Return shopping')
    def test_continue_shopping_button(self, driver):
        with allure.step('Login'):
            login_page = LoginPage(driver)
            login_page.go_to_login_page()
            login_page.send_user_name()
            login_page.send_password()
            login_page.click_login_button()
            product_page = ProductPage(driver)
            assert product_page.should_be_right_title(PRODUCTS_TITLE)
        with allure.step('Add to cart'):
            product_page.add_product_to_cart_from_products_page(IND)
            product_page.go_to_cart()
            cart_page = CartPage(driver)
            assert cart_page.should_be_right_title(CART_TITLE)
        with allure.step('Continue shopping'):
            cart_page.continue_shopping_button()
            assert product_page.should_be_right_title(PRODUCTS_TITLE)

    @allure.story('Price filter')
    def test_price_filter(self, driver):
        with allure.step('Login'):
            login_page = LoginPage(driver)
            login_page.go_to_login_page()
            login_page.send_user_name()
            login_page.send_password()
            login_page.click_login_button()
            product_page = ProductPage(driver)
            assert product_page.should_be_right_title(PRODUCTS_TITLE)
        with allure.step('Price filter'):
            product_page.select_sort_by_price_from_low()
            low_high_list = product_page.get_list_of_products_titles()
            product_page.select_sort_by_price_from_high()
            high_low_list = product_page.get_list_of_products_titles()
            assert product_page.should_be_correct_sorting(low_high_list, high_low_list)
