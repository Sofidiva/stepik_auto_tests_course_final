import time

from pages.base_page import BasePage
from pages.locators import ProductPageLocators



class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()
        #time.sleep(5)

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "The button 'Add to basket' is not presented"

    def should_be_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_BASKET), "Price is not presented"
        assert self.is_element_present(*ProductPageLocators.NAME_IN_BASKET), "Name is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "Message is not presented"

    def check_product_in_basket(self):
        product_price_on_card = self.browser.find_element(*ProductPageLocators.PRICE_ON_CARD).text
        product_name_on_card = self.browser.find_element(*ProductPageLocators.NAME_ON_CARD).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET).text
        assert product_price_on_card == product_price_in_basket, "Price is incorrect"
        assert product_name_on_card == product_name_in_basket, "Name is incorrect"

    # проверка отсутствие элемента
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    # проверка того, что какой-то элемент исчезает
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should disappear"
