from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner .basket-title")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASS_AGAIN = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form button")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    TEXT_ADD_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages strong")
    TEXT_ADD_TO_BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info p strong")
