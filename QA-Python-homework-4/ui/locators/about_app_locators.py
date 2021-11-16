from appium.webdriver.common.mobileby import MobileBy


class AboutAppPageLocators:
    VERSION_LOCATOR = (
        MobileBy.ID,
        'ru.mail.search.electroscope:id/about_version'
    )

    COPYRIGHT_LOCATOR = (
        MobileBy.ID,
        'ru.mail.search.electroscope:id/about_copyright'
    )
