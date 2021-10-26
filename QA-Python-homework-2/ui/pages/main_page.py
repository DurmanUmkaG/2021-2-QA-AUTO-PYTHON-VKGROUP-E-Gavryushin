from selenium.common.exceptions import TimeoutException

from ui.locators.main_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators

    def click_create_campaign(self):
        try:
            self.click(self.locators.CREATE_CAMPAIGN_NEW_USER)
        except TimeoutException:
            self.click(self.locators.CREATE_CAMPAIGN_BUTTON)
