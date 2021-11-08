import allure
from selenium.common.exceptions import TimeoutException

from ui.locators.main_locators import MainPageLocators
from ui.pages.audiences_page import AudiencesPage
from ui.pages.base_page import BasePage
from ui.pages.campaign_creation_page import CampaignCreationPage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    locators = MainPageLocators

    @allure.step('Going to campaign_creation_page')
    def click_create_campaign(self):
        try:
            self.click(self.locators.CREATE_CAMPAIGN_NEW_USER)
        except TimeoutException:
            self.click(self.locators.CREATE_CAMPAIGN_BUTTON)
        return CampaignCreationPage(self.driver)

    @allure.step('Going to audiences_page')
    def go_to_audiences_page(self):
        self.click(self.locators.AUDIENCES_LOCATOR)
        return AudiencesPage(self.driver)

    @allure.step('Deleting campaign {campaign_name}')
    def delete_campaign(self, campaign_name):
        data_row_id = self.find(self.locators.CAMPAIGN_NAME_TEMPLATE(campaign_name)).get_attribute('data-row-id')
        self.click(self.locators.CAMPAIGN_CHECKBOX_LOCATOR_TEMPLATE(data_row_id))
        self.click(self.locators.CAMPAIGN_ACTIONS_LOCATOR)
        self.click(self.locators.CAMPAIGN_DELETE_LOCATOR)
        self.wait().until(EC.presence_of_element_located(self.locators.CAMPAIGN_DELTED_NOTIFICATION_LOCATOR))
