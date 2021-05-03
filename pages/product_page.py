from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button.click()
        # self.solve_quiz_and_get_code()

    def should_be_right_basket_messages(self):
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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.TEXT_ADD_TO_BASKET_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.TEXT_ADD_TO_BASKET_PRODUCT_NAME), \
            "Success message is not disappeared, but should be"




    # def should_be_equal_elem1_and_elem2(self, elem1, elem2):
    #     element1 = self.browser.find_element(*elem1)
    #     element2 = self.browser.find_element(*elem2)
    #     assert element1.text == element2.text, f'{} and {} is not equal'
    #
    # def should_be_right_basket_messages(self):
    #     self.should_be_equal_elem1_and_elem2(ProductPageLocators.PRODUCT_NAME,
    #                                          ProductPageLocators.TEXT_ADD_TO_BASKET_PRODUCT_NAME)
    #     self.should_be_equal_elem1_and_elem2(ProductPageLocators.PRODUCT_PRICE,
    #                                          ProductPageLocators.TEXT_ADD_TO_BASKET_PRODUCT_PRICE)
