from selenium.webdriver.common.by import By

class QuestionsLocators:
    COOKIE_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")
    FIRST_QUESTION = (By.XPATH, "//div[@id='accordion__heading-0']")  # первый вопрос "Сколько это стоит? И как оплатить?"
    FIRST_QUESTION_ANSWER = (By.XPATH, "// p[contains(text(), 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]")  # ответ на первый вопрос
    SECOND_QUESTION = (By.XPATH, "//div[@id='accordion__heading-1']")  # второй вопрос "Хочу сразу несколько самокатов! Так можно?
    SECOND_QUESTION_ANSWER = (By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')]")
    THIRD_QUESTION = (By.XPATH, "//div[@id='accordion__heading-2']")  # третий вопрос "Как рассчитывается время аренды?"
    THIRD_QUESTION_ANSWER = (By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')]")
    FOURTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-3']")  # четвертый вопрос "Можно ли заказать самокат прямо на сегодня?"
    FOURTH_QUESTION_ANSWER = (By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')]")
    FIFTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-4']")  # пятый вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    FIFTH_QUESTION_ANSWER = (By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')]")
    SIXTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-5']")  # шестой вопрос "Вы привозите зарядку вместе с самокатом?"
    SIXTH_QUESTION_ANSWER = (By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')]")
    SEVENTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-6']")  # седьмой вопрос "Можно ли отменить заказ?"
    SEVENTH_QUESTION_ANSWER = (By.XPATH, "//*[@id='accordion__panel-6']")  # 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')]"
    EIGHTH_QUESTION = (By.XPATH, "//*[@id='accordion__heading-7']")  # восьмой вопрос "Я живу за МКАДом, привезёте?"
    EIGHTH_QUESTION_ANSWER = (By.XPATH, "//*[@id='accordion__panel-7']")  # "Да, обязательно. Всем самокатов! И Москве, и Московской области."
