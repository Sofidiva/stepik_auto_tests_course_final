from pages.product_page import ProductPage

#link = 'https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.add_to_basket()
    page.should_be_product_in_basket()
    page.check_product_in_basket()
