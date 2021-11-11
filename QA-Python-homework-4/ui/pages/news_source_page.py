from ui.locators.news_source_locators import NewsSourcePageLocators
from ui.pages.base_page import BasePage


class NewsSourcePage(BasePage):
    locators = NewsSourcePageLocators

    def choose_news_source(self):
        self.click(self.locators.NEWS_SOURCE_LOCATOR)
        assert self.find(self.locators.CHECK_MARK_LOCATOR).is_displayed()
        self.click(self.locators.ARROW_LOCATOR)
