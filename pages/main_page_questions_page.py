from base.base_object import BaseObject
from locators.main_page_questions_locators import QuestionsLocators
import allure


class QuestionMainPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('accept cookies')
    def click_to_accept_cookies(self):
        self.to_click(QuestionsLocators.COOKIE_BUTTON)

    @allure.step('click to first question title')
    def click_first_question(self):
        self.to_click(QuestionsLocators.FIRST_QUESTION)

    @allure.step('get answer for the first question')
    def get_answer_first_question(self):
        return self.get_text_of_element(QuestionsLocators.FIRST_QUESTION_ANSWER)

    @allure.step('click to second question title')
    def click_second_question(self):
        self.to_click(QuestionsLocators.SECOND_QUESTION)

    @allure.step('get answer for the second question')
    def get_answer_second_question(self):
        return self.get_text_of_element(QuestionsLocators.SECOND_QUESTION_ANSWER)

    @allure.step('click to third question title')
    def click_third_question(self):
        self.to_click(QuestionsLocators.THIRD_QUESTION)

    @allure.step('get answer for the third question')
    def get_answer_third_question(self):
        return self.get_text_of_element(QuestionsLocators.THIRD_QUESTION_ANSWER)

    @allure.step('click to fourth question title')
    def click_fourth_question(self):
        self.to_click(QuestionsLocators.FOURTH_QUESTION)

    @allure.step('get answer for the fourth question')
    def get_answer_fourth_question(self):
        return self.get_text_of_element(QuestionsLocators.FOURTH_QUESTION_ANSWER)

    @allure.step('click to fifth question title')
    def click_fifth_question(self):
        self.to_click(QuestionsLocators.FIFTH_QUESTION)

    @allure.step('get answer for the fifth question')
    def get_answer_fifth_question(self):
        return self.get_text_of_element(QuestionsLocators.FIFTH_QUESTION_ANSWER)

    @allure.step('click to sixth question title')
    def click_sixth_question(self):
        self.to_click(QuestionsLocators.SIXTH_QUESTION)

    @allure.step('get answer for the sixth question')
    def get_answer_sixth_question(self):
        return self.get_text_of_element(QuestionsLocators.SIXTH_QUESTION_ANSWER)

    @allure.step('click to seventh question title')
    def click_seventh_question(self):
        self.to_click(QuestionsLocators.SEVENTH_QUESTION)

    @allure.step('get answer for the seventh question')
    def get_answer_seventh_question(self):
        return self.get_text_of_element(QuestionsLocators.SEVENTH_QUESTION_ANSWER)

    @allure.step('click to eighth question title')
    def click_eighth_question(self):
        self.to_click(QuestionsLocators.EIGHTH_QUESTION)

    @allure.step('get answer for the eighth question')
    def get_answer_eighth_question(self):
        return self.get_text_of_element(QuestionsLocators.EIGHTH_QUESTION_ANSWER)


