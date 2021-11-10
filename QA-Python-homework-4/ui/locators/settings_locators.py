from appium.webdriver.common.mobileby import MobileBy


class SettingsPageLocators:
    NEWS_SOURCE_LOCATOR = (
        MobileBy.ID,
        'ru.mail.search.electroscope:id/user_settings_field_news_sources'
    )
