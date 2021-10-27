from selenium.common.exceptions import TimeoutException

from ui.locators.main_locators import MainPageLocators
from ui.pages.audiences_page import AudiencesPage
from ui.pages.base_page import BasePage
from ui.pages.campaign_creation_page import CampaignCreationPage


class MainPage(BasePage):
    locators = MainPageLocators

    def click_create_campaign(self):
        try:
            self.click(self.locators.CREATE_CAMPAIGN_NEW_USER)
        except TimeoutException:
            self.click(self.locators.CREATE_CAMPAIGN_BUTTON)
        return CampaignCreationPage(self.driver)

    def go_to_audiences_page(self):
        self.click(self.locators.AUDIENCES_LOCATOR)
        return AudiencesPage(self.driver)