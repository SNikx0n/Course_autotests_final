from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        pass_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS)
        pass_again_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS_AGAIN)
        email_form.send_keys(email)
        pass_form.send_keys(password)
        pass_again_form.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Is not login url"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
