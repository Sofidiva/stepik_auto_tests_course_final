import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxProfile


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: '--language=en' or '--language=ru' or '--language=es'")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    options_ff = FirefoxProfile()
    options_ff.set_preference("intl.accept_languages", user_language)
    options_ff.binary_location = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_ff)
        # browser = webdriver.Firefox(executable_path=r'C:\FirefoxDriver\geckodriver.exe')
        # browser = webdriver.Firefox(firefox_profile=fp)
        #browser = webdriver.Firefox(firefoxOptions=options_ff)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()