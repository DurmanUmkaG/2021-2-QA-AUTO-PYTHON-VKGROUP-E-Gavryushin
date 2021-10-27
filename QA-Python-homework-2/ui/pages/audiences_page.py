import time

from selenium.common.exceptions import TimeoutException

from ui.locators.audiences_locators import AudiencesLocators
from ui.pages.base_page import BasePage


class AudiencesPage(BasePage):
    locators = AudiencesLocators

    def create_segment(self):
        try:
            self.click(self.locators.CREATE_NEW)
        except TimeoutException:
            self.click(self.locators.CREATE_ALREADY_EXIST)
        if self.find(self.locators.ADDING_SEGMENTS_LOCATOR).text.lower() == 'adding segments':
            self.click(self.locators.APPS_AND_GAMES_ENG_SEGMENTS)
        else:
            self.click(self.locators.APPS_AND_GAMES_RU_SEGMENTS)
        self.click(self.locators.PLAYED_AND_PAID_CHECKBOX)
        self.click(self.locators.ADD_SEGMENT_BUTTON)
        segment_name = self.create_random_str()
        self.send_keys(self.locators.SEGMENT_NAME_INPUT_LOCATOR, segment_name)
        self.click(self.locators.CREATE_SEGMENT_BUTTON)
        return segment_name
