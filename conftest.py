import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.order_page import OrderPage
from pages.main_page_questions_page import QuestionMainPage




@pytest.fixture
def get_firefox_options():
    options = firefox_options()
    return options

@pytest.fixture
def get_webdriver(get_firefox_options):
    options = get_firefox_options
    driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
    driver.set_window_size(1920,1080)
    return driver

@pytest.fixture
def setup(get_webdriver):
    URL = 'https://qa-scooter.praktikum-services.ru/'
    get_webdriver.get(URL)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def order_page(setup):
    yield OrderPage(setup)

@pytest.fixture
def main_page_question_page(setup):
    yield QuestionMainPage(setup)




