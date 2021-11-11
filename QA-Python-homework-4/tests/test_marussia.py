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
