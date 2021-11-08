from selenium.webdriver.common.by import By


class BasePageLocators:
    SPINNER_LOCATOR = (By.XPATH, '//div[contains(@class, "spinner")]')