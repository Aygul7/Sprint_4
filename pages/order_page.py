from base.base_object import BaseObject
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('accept cookies')
    def click_to_accept_cookies(self):
        self.to_click(OrderPageLocators.COOKIE_BUTTON)

    @allure.step('clicking to upper order button')
    def click_to_upper_order_button(self):
        self.to_click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('clicking to lower order button')
    def click_to_lower_order_button(self):
        self.to_click(OrderPageLocators.MAIN_PAGE_LOWER_ORDER_BUTTON)

    @allure.step('set up name Мария')
    def set_name_first_set(self):
        self.set_value(OrderPageLocators.NAME_FIELD, 'Мария')

    @allure.step('set up name Иван')
    def set_name_second_set(self):
        self.set_value(OrderPageLocators.NAME_FIELD, 'Иван')

    @allure.step('set up surname Катина')
    def set_surname_first_set(self):
        self.set_value(OrderPageLocators.SURNAME_FIELD, 'Катина')

    @allure.step('set up surname Петров')
    def set_surname_second_set(self):
        self.set_value(OrderPageLocators.SURNAME_FIELD, 'Петров')

    @allure.step('set up address Московская, 10')
    def set_address_first_set(self):
        self.set_value(OrderPageLocators.ADDRESS_FIELD, 'Московская, 10')

    @allure.step('set up address Кремлевская, 20')
    def set_address_second_set(self):
        self.set_value(OrderPageLocators.ADDRESS_FIELD, 'Кремлевская, 20')

    @allure.step('click on field of metro station')
    def set_metro_station(self):
        self.to_click(OrderPageLocators.METRO_STATION_FIELD)

    @allure.step('choose Bulvard metro station')
    def choose_metro_station_first_set(self):
        self.to_click(OrderPageLocators.BULVARD_STATION)

    @allure.step('choose Cherkizovskaya metro station')
    def choose_metro_station_second_set(self):
        self.to_click(OrderPageLocators.CHERKIZOVSKAYA_STATION)

    @allure.step('set up phone number')
    def set_phone_number_first_set(self):
        self.set_value(OrderPageLocators.PHONE_FIELD, '91234567890')

    @allure.step('set up phone number')
    def set_phone_number_second_set(self):
        self.set_value(OrderPageLocators.PHONE_FIELD, '91133344555')

    @allure.step('click to button Next')
    def click_button_next(self):
        self.to_click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('click to calendar field')
    def click_calendar_field(self):
        self.to_click(OrderPageLocators.WHEN_BRING_SCOOTER_FIELD)

    @allure.step('choose day, when to bring scooter')
    def click_day_16_january(self):
        self.to_click(OrderPageLocators.DAY16_JANUARY)

    @allure.step('choose day, when to bring scooter')
    def click_day_17_january(self):
        self.to_click(OrderPageLocators.DAY17_JANUARY)

    @allure.step('click to the field with order period')
    def click_order_period_field(self):
        self.to_click(OrderPageLocators.ORDER_PERIOD_FIELD)

    @allure.step('choose two days for order period')
    def choose_two_days_to_order(self):
        self.to_click(OrderPageLocators.ORDER_TWO_DAYS)

    @allure.step('choose one day for order period')
    def choose_one_day_to_order(self):
        self.to_click(OrderPageLocators.ORDER_ONE_DAY)

    @allure.step('choose black colour of the scooter')
    def choose_black_colour_scooter(self):
        self.to_click(OrderPageLocators.BLACK_SCOOTER)

    @allure.step('choose black colour of the scooter')
    def choose_grey_colour_scooter(self):
        self.to_click(OrderPageLocators.GREY_SCOOTER)

    @allure.step('set comment')
    def set_comment_first_set(self):
        self.set_value(OrderPageLocators.COMMENT_FIELD, 'Привет! ждем самокат!')

    @allure.step('set comment')
    def set_comment_second_set(self):
        self.set_value(OrderPageLocators.COMMENT_FIELD, 'Hello, World!')

    @allure.step('click lower button Order')
    def click_lower_button_order(self):
        self.to_click(OrderPageLocators.ORDER_PAGE_LOWER_ORDER_BUTTON)

    @allure.step('click Yes to confirm order')
    def click_yes_confirm_order(self):
        self.to_click(OrderPageLocators.ORDER_MODAL_YES_BUTTON)

    @allure.step('get text of the page to check order result')
    def get_text_of_page(self):
        return self.get_text_of_element(OrderPageLocators.CHECK_ORDER_STATUS_BUTTON)

    @allure.step('click to button check status')
    def click_check_status_button(self):
        self.to_click(OrderPageLocators.CHECK_ORDER_STATUS_BUTTON)

    @allure.step('click to scooter logo')
    def click_scooter_logo(self):
        self.to_click(OrderPageLocators.SCOOTER_LOGO)

    @allure.step('click to yandex logo')
    def click_yandex_logo(self):
        self.to_click(OrderPageLocators.YANDEX_TEXT)

    @allure.step('move to new yandex page')
    def move_to_new_yandex_page(self):
        yandex_page = self.driver.window_handles[1]
        self.driver.switch_to.window(yandex_page)

    @allure.step('check yandex url')
    def get_yandex_url(self):
        self.get_url('https://dzen.ru/?yredirect=true')

    @allure.step('check scooter url')
    def get_scooter_url(self):
        self.get_url('https://qa-scooter.praktikum-services.ru/')






















