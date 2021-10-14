from ui.pages.base_page import BasePage
from ui.locators.main_locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators

    def logout(self):
        self.click(self.locators.BALANCE_LOCATOR)
        self.click(self.locators.LOG_OF_LOCATOR)
