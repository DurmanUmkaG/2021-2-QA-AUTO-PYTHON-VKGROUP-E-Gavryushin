from selenium.webdriver.common.by import By


class MainPageLocators:
    CREATE_CAMPAIGN_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "dashboard-module-createButtonWrap")]//div'
    )

    CREATE_CAMPAIGN_NEW_USER = (
        By.XPATH,
        '//a[@href="/campaign/new"]'
    )

    CAMPAIGN_NAME_TEMPLATE = lambda x:(By.XPATH, f'//a[@title="{x}"]')

    AUDIENCES_LOCATOR = (By.XPATH, '//a[@href="/segments"]')
