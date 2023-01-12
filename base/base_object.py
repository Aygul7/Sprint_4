from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class BaseObject:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def to_click(self, locator):
        self.is_clickable(locator).click()

    def set_value(self,locator, value):
        self.is_clickable(locator).send_keys(value)

    def get_text_of_element(self, locator):
        return self.is_clickable(locator).text

    def get_url(self, url):
        return self.wait.until(ec.url_to_be(url))






















