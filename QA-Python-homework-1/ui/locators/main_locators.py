from selenium.webdriver.common.by import By


class MainPageLocators:
    BALANCE_LOCATOR = (By.XPATH, '//div[contains(text(), "Balance")]')
    LOG_OF_LOCATOR = (By.XPATH, '//a[contains(text(), "Log off")]')
