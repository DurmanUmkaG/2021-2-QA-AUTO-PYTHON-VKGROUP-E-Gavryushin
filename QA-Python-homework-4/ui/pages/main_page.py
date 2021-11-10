from ui.locators.main_locators import MainPageLocators
from ui.pages.base_page import BasePage
from ui.pages.settings_page import SettingsPage


class MainPage(BasePage):
    locators = MainPageLocators

    def get_population(self):
        self.click(self.locators.KEYBOARD_BUTTON)

        for i in range(2):
            self.send_keys(self.locators.INPUT_FIELD_LOCATOR, 'Russia')
            self.click(self.locators.SEND_TEXT_BUTTON)

        assert self.find(self.locators.RUSSIA_BLOCK_LOCATOR).is_displayed()

        self.swipe_to_element(
            self.swipe_element_to_left,
            self.locators.SUGGEST_ITEM_TEMPLATE_LOCATOR('население россии'),
            self.locators.SUGGEST_ITEM_TEMPLATE_LOCATOR('Нет')
        )

        self.click(self.locators.SUGGEST_ITEM_TEMPLATE_LOCATOR('население россии'))

        return self.find(self.locators.RUSSIAN_POPULATION_LOCATOR).get_attribute('text')

    def get_calculation_result(self, number1, number2):
        self.click(self.locators.KEYBOARD_BUTTON)
        self.send_keys(self.locators.INPUT_FIELD_LOCATOR, f'{number1} + {number2}')
        self.click(self.locators.SEND_TEXT_BUTTON)
        return self.find(self.locators.SUGGEST_ITEM_TEMPLATE_LOCATOR(str(number1 + number2))).get_attribute('text')

    def go_to_settings_page(self):
        self.click(self.locators.SETTINGS_BUTTON)
        return SettingsPage(self.driver)
