from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOG_IN_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    USERNAME_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
