from ui.locators.main_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators

    def get_population(self):
        self.click(self.locators.KEYBOARD_BUTTON)
        for i in range(2):
            self.send_keys(self.locators.INPUT_FIELD_LOCATOR, 'Russia')
            self.click(self.locators.SEND_TEXT_BUTTON)
        assert self.find(self.locators.RUSSIA_BLOCK_LOCATOR).is_displayed()
        self.swipe_to_element(
            self.locators.SUGGEST_ITEM_TEMPLATE_LOCATOR('Нет'),
            self.locators.SUGGEST_ITEM_TEMPLATE_LOCATOR('население россии'),
            10
        )
        self.click(self.locators.SUGGEST_ITEM_TEMPLATE_LOCATOR('население россии'))
        return self.find(self.locators.RUSSIAN_POPULATION_LOCATOR).get_attribute('text')
