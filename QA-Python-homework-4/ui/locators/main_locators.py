from appium.webdriver.common.mobileby import MobileBy


class MainPageLocators:
    KEYBOARD_BUTTON = (
        MobileBy.ID,
        'ru.mail.search.electroscope:id/keyboard'
    )

    INPUT_FIELD_LOCATOR = (
        MobileBy.ID,
        'ru.mail.search.electroscope:id/input_text'
    )

    SUGGEST_ITEM_TEMPLATE_LOCATOR = lambda x: (
        MobileBy.XPATH,
        f'//android.widget.TextView[@text="{x}"]'
    )

    SEND_TEXT_BUTTON = (
        MobileBy.ID,
        'ru.mail.search.electroscope:id/text_input_action'
    )

    RUSSIAN_POPULATION_LOCATOR = (
        MobileBy.ID,
        'ru.mail.search.electroscope:id/item_dialog_fact_card_content_text'
    )

    RUSSIA_BLOCK_LOCATOR = (
        MobileBy.ID,
        'ru.mail.search.electroscope:id/item_dialog_fact_card_content_block'
    )
