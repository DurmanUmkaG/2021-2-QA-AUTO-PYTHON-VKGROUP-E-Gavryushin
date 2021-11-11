from ui.locators.settings_locators import SettingsPageLocators
from ui.pages.about_app_page import AboutAppPage
from ui.pages.base_page import BasePage
from ui.pages.news_source_page import NewsSourcePage


class SettingsPage(BasePage):
    locators = SettingsPageLocators

    def go_to_news_source_page(self):
        self.swipe_to_element(self.swipe_up, self.locators.NEWS_SOURCE_LOCATOR)
        self.click(self.locators.NEWS_SOURCE_LOCATOR)
        return NewsSourcePage(self.driver)

    def go_to_about_app_page(self):
        self.swipe_to_element(self.swipe_up, self.locators.ABOUT_APP_LOCATOR)
        self.click(self.locators.ABOUT_APP_LOCATOR)
        return AboutAppPage(self.driver)
