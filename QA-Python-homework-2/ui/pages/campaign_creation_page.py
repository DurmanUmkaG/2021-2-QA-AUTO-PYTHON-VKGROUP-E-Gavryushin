import os.path

from ui.locators.campaign_creation_locators import CampaignCreationLocators
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CampaignCreationPage(BasePage):
    locators = CampaignCreationLocators

    def fill_url(self):
        self.send_keys(
            self.locators.CAMPAIGN_LINK_INPUT_LOCATOR,
            self.create_random_str() + '.ru'
        )

    def fill_campaign_name(self):
        name = self.create_random_str()
        self.send_keys(
            self.locators.CAMPAIGN_NAME_INPUT_LOCATOR,
            name
        )
        return name

    def upload_image(self, repo_root):
        file = os.path.join(repo_root, 'files', 'image.jpg')
        self.find(self.locators.UPLOAD_IMAGE_BUTTON).send_keys(file)

    def create_campaign(self, repo_root):
        self.click(self.locators.TRAFFIC_BUTTON)
        self.fill_url()
        self.wait(20).until(EC.visibility_of_element_located(self.locators.CAMPAIGN_NAME_LOCATOR))
        campaign_name = self.fill_campaign_name()
        self.click(self.locators.BANNER_BUTTON)
        self.upload_image(repo_root)
        self.click(self.locators.CREATE_A_CAMPAIGN_BUTTON)
        return campaign_name