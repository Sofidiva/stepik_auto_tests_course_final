import random
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest
from faker import Faker

link = 'https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'          # 4_3_2
#link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'           # 4_3_3
@pytest.mark.registration
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        self.login_page.go_to_login_page()
        fake = Faker()
        email = fake.email()
        password = fake.password(length = random.randint(9, 15))
        self.login_page.register_new_user(email=email, password=password)
        self.login_page.user_should_be_authorized()
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket()
        page.add_to_basket()
        page.should_be_product_in_basket()
        page.check_product_in_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


#@pytest.mark.skip
@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6",
                                         pytest.param("7", marks=pytest.mark.xfail), "8", "9"])

#@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.add_to_basket()
    page.should_be_product_in_basket()
    page.check_product_in_basket()

@pytest.mark.xfail(reason="Success message is presented, but should not be")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.add_to_basket()
    page.should_not_be_success_message()

#@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Success message is presented, but should disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.add_to_basket()
    page.should_disappear_success_message()


# 4.3.8
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# 4.3.8
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

# 4.3.10
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_is_empty_message()
    page.should_not_be_items_in_basket()
