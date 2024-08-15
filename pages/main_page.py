from pages.base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
#from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

'''метод __init__ вызывается при создании объекта. 
Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка и 
передает ему все те аргументы, которые мы передали в конструктор MainPage. '''