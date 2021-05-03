from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button.click()
        # self.solve_quiz_and_get_code()

    def right_basket_messages(self):
        self.should_be_right_product_name()
        self.should_be_equal_price_basket_product()

    def should_be_right_product_name(self):
        message_add_to_basket_name = self.browser.find_element(*ProductPageLocators.TEXT_ADD_TO_BASKET_PRODUCT_NAME)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert message_add_to_basket_name.text == product_name.text, 'Product name is not correct'

    def should_be_equal_price_basket_product(self):
        message_add_to_basket_price = self.browser.find_element(*ProductPageLocators.TEXT_ADD_TO_BASKET_PRODUCT_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert message_add_to_basket_price.text == product_price.text, 'Product price is not correct'