from selenium.webdriver.common.by import By


class AudiencesLocators:
    CREATE_NEW = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    CREATE_ALREADY_EXIST = (By.CLASS_NAME, "button__text")

    # Использую 2 локатора для обеих локализаций,
    # т.к. не на что натравиться кроме title
    APPS_AND_GAMES_RU_SEGMENTS = (
        By.XPATH,
        '//div[contains(text(), "Приложения и игры")]'
    )
    APPS_AND_GAMES_ENG_SEGMENTS = (
        By.XPATH,
        '//div[contains(text(), "Apps and games")]'
    )

    ADDING_SEGMENTS_LOCATOR = (By.CLASS_NAME, 'js-modal-title')

    PLAYED_AND_PAID_CHECKBOX = (
        By.XPATH,
        '//input[@type="checkbox"]'
    )

    ADD_SEGMENT_BUTTON = (
        By.XPATH,
        '//div[@class="adding-segments-modal__btn-wrap js-add-button"]/button'
    )

    SEGMENT_NAME_INPUT_LOCATOR = (
        By.XPATH,
        '//input[@class="input__inp js-form-element" and @maxlength="60"]'
    )

    CREATE_SEGMENT_BUTTON = (
        By.XPATH,
        '//div[@class="create-segment-form__btn-wrap js-create-segment-button-wrap"]/button'
    )

    SEGMENT_IN_LIST_TEMPLATE = (
        By.XPATH,
        '//div[./a[@title="{}"]]/..'
    )

    DELETE_SEGMENT_TEMPLATE = (
        By.XPATH,
        '//div[@data-row-id="{}"]/span'
    )

    DELETE_BUTTON = (
        By.XPATH,
        '//button[@class="button button_confirm-remove button_general"]'
    )

    DELETE_MESSAGE_LOCATOR = (
        By.CLASS_NAME,
        'modal-view__body__placeholder'
    )
