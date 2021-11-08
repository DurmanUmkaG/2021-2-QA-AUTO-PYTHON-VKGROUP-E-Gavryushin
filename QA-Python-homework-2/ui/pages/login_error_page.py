from ui.pages.base_page import BasePage
from ui.locators.login_error_locators import LoginErrorLocators


class LoginErrorPage(BasePage):
    locators = LoginErrorLocators
    url = 'https://account.my.com/login/'
