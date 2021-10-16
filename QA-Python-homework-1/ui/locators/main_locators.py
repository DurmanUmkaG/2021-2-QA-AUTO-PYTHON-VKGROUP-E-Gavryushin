from selenium.webdriver.common.by import By


class MainPageLocators:
    BALANCE_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-infoWrap")]')
    LOG_OF_LOCATOR = (By.XPATH, '//a[contains(@href, "logout")]')
    PROFILE_LOCATOR = (By.XPATH, '//a[contains(@href, "profile")]')
    FULLNAME_LOCATOR = (By.XPATH, '//input[@class="input__inp js-form-element" and @maxlength="100"]')
    PHONE_NUMBER_LOCATOR = (By.XPATH, '//input[@class="input__inp js-form-element" and @maxlength="20"]')
    SAVE_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button button_submit"]')
    SAVE_NOTIFICATION_LOCATOR = (By.XPATH, '//div[@class="_notification__content js-notification-content"]')
    AUDIENCES_LOCATOR = (By.XPATH, '//a[contains(@href, "segments")]')
    AUDIENCE_SEGMENTS_LOCATOR = (By.XPATH, '//span[@class="left-nav__group__label"]')
    PROFILE_SETTINGS_LOCATOR = (By.XPATH, '//span[@class="left-nav__group__label"]')
