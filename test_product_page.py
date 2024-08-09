from pages.product_page import ProductPage
import pytest

#link = 'https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'          # 4_3_2
#link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'           # 4_3_3


@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6",
                                         pytest.param("7", marks=pytest.mark.xfail), "8", "9"])          # 4_3_4

def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"      # 4_3_4
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.add_to_basket()
    page.should_be_product_in_basket()
    page.check_product_in_basket()
