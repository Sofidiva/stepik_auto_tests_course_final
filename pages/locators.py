from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group .btn-default:nth-child(1)")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE_ON_CARD = (By.CSS_SELECTOR, '.product_main .price_color')
    NAME_ON_CARD = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages > .alert:nth-child(3) > .alertinner strong')
    NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) > .alertinner strong')
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) > .alertinner')

