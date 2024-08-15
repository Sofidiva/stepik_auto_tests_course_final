from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert login_word in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_element = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_element.send_keys(email)
        password_element = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_element.send_keys(password)
        confirm_password_element = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password_element.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()


    def user_should_be_authorized(self):
        assert self.is_element_present(*LoginPageLocators.USER_ICON), \
            "The user is not authorized? but should be"