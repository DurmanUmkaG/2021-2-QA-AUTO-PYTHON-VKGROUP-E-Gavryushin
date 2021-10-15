from selenium.webdriver.common.by import By


class MainPageLocators:
    BALANCE_LOCATOR = (By.XPATH, '//div[contains(text(), "Balance")]')
    LOG_OF_LOCATOR = (By.XPATH, '//a[contains(text(), "Log off")]')
    PROFILE_LOCATOR = (By.XPATH, '//a[contains(text(), "Profile")]')
    FULLNAME_LOCATOR = (By.XPATH, '//input[@class="input__inp js-form-element" and @maxlength="100"]')
    PHONE_NUMBER_LOCATOR = (By.XPATH, '//input[@class="input__inp js-form-element" and @maxlength="20"]')
    SAVE_BUTTON_LOCATOR = (By.XPATH, '//div[contains(text(), "Save")]')
    SAVE_NOTIFICATION_LOCATOR = (By.XPATH, '//div[contains(text(), "Information saved successfully")]')
    AUDIENCES_LOCATOR = (By.XPATH, '//a[contains(text(), "Audiences")]')
    AUDIENCE_SEGMENTS_LOCATOR = (By.XPATH, '//span[contains(text(), "Audience segments")]')
    PROFILE_SETTINGS_LOCATOR = (By.XPATH, '//span[contains(text(), "Profile settings")]')
