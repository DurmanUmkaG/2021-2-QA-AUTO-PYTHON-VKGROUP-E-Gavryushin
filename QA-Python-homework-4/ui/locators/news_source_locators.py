from appium.webdriver.common.mobileby import MobileBy


class NewsSourcePageLocators:
    NEWS_SOURCE_LOCATOR = (
        MobileBy.XPATH,
        '//android.widget.TextView[@text="Вести FM"]'
    )

    CHECK_MARK_LOCATOR = (
        MobileBy.ID,
        'ru.mail.search.electroscope:id/news_sources_item_selected'
    )

    ARROW_LOCATOR = (
        MobileBy.XPATH,
        '//android.widget.ImageButton'
    )