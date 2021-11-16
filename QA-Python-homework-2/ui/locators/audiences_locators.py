from selenium.webdriver.common.by import By


class AudiencesLocators:
    CREATE_NEW = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    CREATE_ALREADY_EXIST = (By.CLASS_NAME, "button__text")

    # Использую 2 локатора для обеих локализаций,
    # т.к. не на что натравиться кроме title
    APPS_AND_GAMES_SEGMENTS = lambda x: (
        By.XPATH,
        f'//div[contains(text(), "{x}")]'
    )

    ADDING_SEGMENTS_LOCATOR = (By.CLASS_NAME, 'js-modal-title')

    PLAYED_AND_PAID_CHECKBOX = (
        By.XPATH,
        '//input[@type="checkbox"]'
    )

    ADD_SEGMENT_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "js-add-button")]/button'
    )

    SEGMENT_NAME_INPUT_LOCATOR = (
        By.XPATH,
        '//input[contains(@class, "js-form-element") and @maxlength="60"]'
    )

    CREATE_SEGMENT_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "js-create-segment-button-wrap")]/button'
    )

    SEGMENT_IN_LIST_TEMPLATE = lambda x: (
        By.XPATH,
        f'//div[./a[@title="{x}"]]/..'
    )

    DELETE_SEGMENT_TEMPLATE = lambda x: (
        By.XPATH,
        f'//div[@data-row-id="{x}"]/span'
    )

    DELETE_BUTTON = (
        By.XPATH,
        '//button[contains(@class, "button_general")]'
    )

    DELETE_MESSAGE_LOCATOR = (
        By.CLASS_NAME,
        'modal-view__body__placeholder'
    )
