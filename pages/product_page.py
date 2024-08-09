from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "The button 'Add to basket' is not presented"

    def should_be_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_BASKET), "Price is not presented"
        assert self.is_element_present(*ProductPageLocators.NAME_IN_BASKET), "Name is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "Message is not presented"

    def check_product_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_ON_CARD).text
        product_name = self.browser.find_element(*ProductPageLocators.NAME_ON_CARD).text
        basket_total = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        message_add_to_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET).text
        assert product_price in basket_total, "Price is incorrect"
        assert product_name in message_add_to_basket, "Name is incorrect"


