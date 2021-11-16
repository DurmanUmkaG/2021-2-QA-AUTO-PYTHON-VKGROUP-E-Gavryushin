from ui.locators.about_app_locators import AboutAppPageLocators
from ui.pages.base_page import BasePage


class AboutAppPage(BasePage):
    locators = AboutAppPageLocators

    def get_app_version(self):
        return self.find(self.locators.VERSION_LOCATOR).get_attribute('text').split()[-1]

    def get_trade_mark(self):
        return self.find(self.locators.COPYRIGHT_LOCATOR).get_attribute('text')
