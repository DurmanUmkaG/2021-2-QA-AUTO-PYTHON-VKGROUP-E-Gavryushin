from selenium.webdriver.common.by import By


class CampaignCreationLocators:
    TRAFFIC_BUTTON = (By.XPATH, '//div[contains(@class, "_traffic")]')

    CAMPAIGN_LINK_INPUT_LOCATOR = (By.XPATH, '//input[@data-gtm-id="ad_url_text"]')

    CAMPAIGN_NAME_INPUT_LOCATOR = (
        By.XPATH,
        '//div[contains(@class,"input_with-close")]/div[@class="input__wrap"]/input'
    )

    BANNER_BUTTON = (By.ID, "patterns_banner_4")

    UPLOAD_IMAGE_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "bannerForm-module-roleInline")]//div[contains(@class, "upload-module-wrapper")]/input'
    )

    CAMPAIGN_NAME_LOCATOR = (By.CLASS_NAME, "campaign-name__title")

    CREATE_A_CAMPAIGN_BUTTON = (By.XPATH, '//div[contains(@class, "js-save-button-wrap")]/button')
