from tests.base import BaseCase


class Test(BaseCase):
    def test_population(self):
        assert '146' in self.main_page.get_population()

    def test_calculation(self):
        expression = self.create_random_expression()
        assert self.main_page.get_calculation_result(
            expression['number1'],
            expression['number2']) == str(expression["result"])

    def test_news_source(self):
        assert self.main_page.get_news_source() == 'Вести ФМ'

    def test_app_version(self, apk_path):
        settings_page = self.main_page.go_to_settings_page()
        about_app_page = settings_page.go_to_about_app_page()
        assert about_app_page.get_app_version() in apk_path

    def test_trade_mark(self):
        settings_page = self.main_page.go_to_settings_page()
        about_app_page = settings_page.go_to_about_app_page()
        assert 'Все права защищены' in about_app_page.get_trade_mark()
