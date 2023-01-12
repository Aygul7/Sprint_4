import allure

#тест 5 - первый вопрос раздела "Вопросы о важном"
@allure.description('Check answer to the first question')
@allure.label('owner', 'Aygul')
@allure.title('Check answer to the first question')
@allure.suite('Questions pack')
def test_first_question(main_page_question_page):
    main_page_question_page.click_to_accept_cookies()
    main_page_question_page.click_first_question()
    first_answer = main_page_question_page.get_answer_first_question()
    assert first_answer == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

#тест 6 - второй вопрос раздела "Вопросы о важном"
@allure.description('Check answer to the second question')
@allure.label('owner', 'Aygul')
@allure.title('Check answer to the second question')
@allure.suite('Questions pack')
def test_second_question(main_page_question_page):
    main_page_question_page.click_to_accept_cookies()
    main_page_question_page.click_second_question()
    second_answer = main_page_question_page.get_answer_second_question()
    assert second_answer == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

#тест 7 - третий вопрос раздела "Вопросы о важном"
@allure.description('Check answer to the third question')
@allure.label('owner', 'Aygul')
@allure.title('Check answer to the third question')
@allure.suite('Questions pack')
def test_third_question(main_page_question_page):
    main_page_question_page.click_to_accept_cookies()
    main_page_question_page.click_third_question()
    third_answer = main_page_question_page.get_answer_third_question()
    assert third_answer == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

#тест 8 - четвертый вопрос раздела "Вопросы о важном"
@allure.description('Check answer to the fourth question')
@allure.label('owner', 'Aygul')
@allure.title('Check answer to the fourth question')
@allure.suite('Questions pack')
def test_fourth_question(main_page_question_page):
    main_page_question_page.click_to_accept_cookies()
    main_page_question_page.click_fourth_question()
    fourth_answer = main_page_question_page.get_answer_fourth_question()
    assert fourth_answer == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

#тест 9 - пятый вопрос раздела "Вопросы о важном"
@allure.description('Check answer to the fifth question')
@allure.label('owner', 'Aygul')
@allure.title('Check answer to the fifth question')
@allure.suite('Questions pack')
def test_fifth_question(main_page_question_page):
    main_page_question_page.click_to_accept_cookies()
    main_page_question_page.click_fifth_question()
    fifth_answer = main_page_question_page.get_answer_fifth_question()
    assert fifth_answer == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

#тест 10 - шестой вопрос раздела "Вопросы о важном"
@allure.description('Check answer to the sixth question')
@allure.label('owner', 'Aygul')
@allure.title('Check answer to the sixth question')
@allure.suite('Questions pack')
def test_sixth_question(main_page_question_page):
    main_page_question_page.click_to_accept_cookies()
    main_page_question_page.click_sixth_question()
    sixth_answer = main_page_question_page.get_answer_sixth_question()
    assert sixth_answer == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

#тест 11 - седьмой вопрос раздела "Вопросы о важном"
@allure.description('Check answer to the seventh question')
@allure.label('owner', 'Aygul')
@allure.title('Check answer to the seventh question')
@allure.suite('Questions pack')
def test_seventh_question(main_page_question_page):
    main_page_question_page.click_to_accept_cookies()
    main_page_question_page.click_seventh_question()
    seventh_answer = main_page_question_page.get_answer_seventh_question()
    assert seventh_answer == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

#тест 12 - восьмой вопрос раздела "Вопросы о важном"
@allure.description('Check answer to the eighth question')
@allure.label('owner', 'Aygul')
@allure.title('Check answer to the eighth question')
@allure.suite('Questions pack')
def test_eighth_question(main_page_question_page):
    main_page_question_page.click_to_accept_cookies()
    main_page_question_page.click_eighth_question()
    eighth_answer = main_page_question_page.get_answer_eighth_question()
    assert eighth_answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'