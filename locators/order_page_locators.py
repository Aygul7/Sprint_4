from selenium.webdriver.common.by import By

class OrderPageLocators:

    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    NAME_FIELD = (By.XPATH, "//*[@placeholder = '* Имя']")
    SURNAME_FIELD = (By.XPATH, "//*[@placeholder = '* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//*[@placeholder = '* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, "//*[@placeholder = '* Станция метро']")
    BULVARD_STATION = (By.XPATH, "//div[text() = 'Бульвар Рокоссовского']")
    CHERKIZOVSKAYA_STATION = (By.XPATH, "//div[text() = 'Черкизовская']")
    PHONE_FIELD = (By.XPATH, "//*[@placeholder = '* Телефон: на него позвонит курьер']")
    COOKIE_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")
    WHEN_BRING_SCOOTER_FIELD = (By.XPATH, "//*[@placeholder = '* Когда привезти самокат']")
    DAY16_JANUARY = (By.XPATH, "//div[contains(text(),'16')]")
    DAY17_JANUARY = (By.XPATH, "//div[contains(text(),'17')]")
    ORDER_PERIOD_FIELD = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
    ORDER_TWO_DAYS = (By.XPATH, "//*[@class = 'Dropdown-menu']//*[2]")  # двое суток
    ORDER_ONE_DAY = (By.XPATH, "//*[@class = 'Dropdown-menu']//*[1]")
    SCOOTER_COLOUR_CHECKBOX = (By.XPATH, "//div[contains(text(),'Цвет самоката')]")
    BLACK_SCOOTER = (By.XPATH, "//input[@id='black']")
    GREY_SCOOTER = (By.XPATH, "//input[@id='grey']")
    COMMENT_FIELD = (By.XPATH, "//*[@placeholder = 'Комментарий для курьера']")
    ORDER_PAGE_LOWER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text() = 'Заказать']")  # верхняя кнопка, как на главной странице
    ORDER_MODAL_YES_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    CHECK_ORDER_STATUS = (By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]/*[text() = 'Заказ оформлен']")
    CHECK_ORDER_STATUS_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_NextButton__1_rCA')]/*[text() = 'Посмотреть статус']")
    MAIN_PAGE_LOWER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]/button[text() = 'Заказать']")

    SCOOTER_LOGO = (By.XPATH, "//div[contains(@class, 'Header_Logo__23yGT')]/*[@class = 'Header_LogoScooter__3lsAR']")
    YANDEX_TEXT = (By.XPATH, "//*[@class='Header_LogoYandex__3TSOI']")
