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

    CAMPAIGN_NAME_TEMPLATE = lambda x: (By.XPATH, f'//a[@title="{x}"]/../..')

    AUDIENCES_LOCATOR = (By.XPATH, '//a[@href="/segments"]')

    CAMPAIGN_CHECKBOX_LOCATOR_TEMPLATE = lambda x: (
        By.XPATH,
        f'//div[@data-row-id="{x}"]//input'
    )

    CAMPAIGN_ACTIONS_LOCATOR = (
        By.XPATH,
        '//div[contains(@class, "tableControls-module-selectControl")]'
    )

    CAMPAIGN_DELETE_LOCATOR = (
        By.XPATH,
        '//li[@data-id="8"]'
    )

    CAMPAIGN_DELTED_NOTIFICATION_LOCATOR = (
        By.XPATH,
        '//div[contains(@class, "dashboard-module-toastBlock")]'
    )

