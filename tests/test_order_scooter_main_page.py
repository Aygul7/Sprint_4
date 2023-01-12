import allure


@allure.description('Order scooter with upper "Order" button and the first set')
@allure.label('owner', 'Aygul')
@allure.title('Order scooter with upper "Order" button and the first set')
@allure.suite('Scooter order pack')
@allure.severity(allure.severity_level.BLOCKER)
# тест 1 - тестирование заказа самоката по верхней кнопке "Заказать", с первым набором данных
def test_order_upper_button(order_page):
    order_page.click_to_accept_cookies()
    order_page.click_to_upper_order_button()
    order_page.set_name_first_set()
    order_page.set_surname_first_set()
    order_page.set_address_first_set()
    order_page.set_metro_station()
    order_page.choose_metro_station_first_set()
    order_page.set_phone_number_first_set()
    order_page.click_button_next()
    order_page.click_calendar_field()
    order_page.click_day_16_january()
    order_page.click_order_period_field()
    order_page.choose_two_days_to_order()
    order_page.choose_black_colour_scooter()
    order_page.set_comment_first_set()
    order_page.click_lower_button_order()
    order_page.click_yes_confirm_order()
    order_result = order_page.get_text_of_page()
    assert order_result == 'Посмотреть статус'


# тест 2 - тестирование заказа самоката по нижней кнопке "Заказать", со вторым набором данных
@allure.description('Order scooter with lower "Order" button and the second set')
@allure.label('owner', 'Aygul')
@allure.title('Order scooter with lower "Order" button and the second set')
@allure.suite('Scooter order pack')
@allure.severity(allure.severity_level.BLOCKER)

def test_order_lower_button(order_page):
    order_page.click_to_accept_cookies()
    order_page.click_to_lower_order_button()
    order_page.set_name_second_set()
    order_page.set_surname_second_set()
    order_page.set_address_second_set()
    order_page.set_metro_station()
    order_page.choose_metro_station_second_set()
    order_page.set_phone_number_second_set()
    order_page.click_button_next()
    order_page.click_calendar_field()
    order_page.click_day_17_january()
    order_page.click_order_period_field()
    order_page.choose_one_day_to_order()
    order_page.choose_grey_colour_scooter()
    order_page.set_comment_second_set()
    order_page.click_lower_button_order()
    order_page.click_yes_confirm_order()
    order_result = order_page.get_text_of_page()
    assert order_result == 'Посмотреть статус'

# тест 3 - тестирование заказа самоката по верхней кнопке "Заказать", с первым набором данных
# и проверкой: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»
@allure.description('Click to Scooter logo after ordering scooter with upper "Order" button, the first set')
@allure.label('owner', 'Aygul')
@allure.title('Check Scooter logo')
@allure.suite('Check logo pack')
@allure.severity(allure.severity_level.BLOCKER)

def test_order_scooter_logo(order_page):
    order_page.click_to_accept_cookies()
    order_page.click_to_upper_order_button()
    order_page.set_name_first_set()
    order_page.set_surname_first_set()
    order_page.set_address_first_set()
    order_page.set_metro_station()
    order_page.choose_metro_station_first_set()
    order_page.set_phone_number_first_set()
    order_page.click_button_next()
    order_page.click_calendar_field()
    order_page.click_day_16_january()
    order_page.click_order_period_field()
    order_page.choose_two_days_to_order()
    order_page.choose_black_colour_scooter()
    order_page.set_comment_first_set()
    order_page.click_lower_button_order()
    order_page.click_yes_confirm_order()
    order_page.click_check_status_button()
    order_page.click_scooter_logo()
    order_page.get_scooter_url()


# тест 4 - тестирование заказа самоката по верхней кнопке "Заказать", с первым набором данных
# и проверкой: если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса
@allure.description('Click to Yandex logo after ordering scooter with upper "Order" button, the first set')
@allure.label('owner', 'Aygul')
@allure.title('Check Yandex logo')
@allure.suite('Check logo pack')
@allure.severity(allure.severity_level.BLOCKER)

def test_yandex_logo(order_page):
    order_page.click_to_accept_cookies()
    order_page.click_to_upper_order_button()
    order_page.set_name_first_set()
    order_page.set_surname_first_set()
    order_page.set_address_first_set()
    order_page.set_metro_station()
    order_page.choose_metro_station_first_set()
    order_page.set_phone_number_first_set()
    order_page.click_button_next()
    order_page.click_calendar_field()
    order_page.click_day_16_january()
    order_page.click_order_period_field()
    order_page.choose_two_days_to_order()
    order_page.choose_black_colour_scooter()
    order_page.set_comment_first_set()
    order_page.click_lower_button_order()
    order_page.click_yes_confirm_order()
    order_page.click_check_status_button()
    order_page.click_yandex_logo()
    order_page.move_to_new_yandex_page()
    order_page.get_yandex_url()















