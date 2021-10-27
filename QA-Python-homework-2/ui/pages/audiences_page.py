import time

from selenium.common.exceptions import TimeoutException

from ui.locators.audiences_locators import AudiencesLocators
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


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

    def delete_segment(self):
        segment_name = self.create_segment()

        data_row_id = self.find(
            (
                self.locators.SEGMENT_IN_LIST_TEMPLATE[0],
                self.locators.SEGMENT_IN_LIST_TEMPLATE[1].format(segment_name)
            )
        ).get_attribute('data-row-id')

        self.click(
            (
                self.locators.DELETE_SEGMENT_TEMPLATE[0],
                self.locators.DELETE_SEGMENT_TEMPLATE[1].format(data_row_id)
            )
        )

        self.click(self.locators.DELETE_BUTTON)
        return segment_name

    def is_segment_deleted(self):
        segment_name = self.delete_segment()
        self.wait().until(EC.invisibility_of_element_located(self.locators.DELETE_MESSAGE_LOCATOR))
        try:
            self.find(
                (
                    self.locators.SEGMENT_IN_LIST_TEMPLATE[0],
                    self.locators.SEGMENT_IN_LIST_TEMPLATE[1].format(segment_name)
                )
            )
            return False
        except TimeoutException:
            return True
