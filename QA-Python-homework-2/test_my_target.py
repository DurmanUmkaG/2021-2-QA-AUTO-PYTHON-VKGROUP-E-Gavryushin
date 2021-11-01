import allure
import pytest

from base import BaseCase
from ui.pages.login_error_page import LoginErrorPage


class Test(BaseCase):

    @allure.epic('All tests')
    @allure.feature('UI test')
    @allure.story('Test wrong password')
    @allure.description("""Negative test with wrong password""")
    @pytest.mark.UI
    def test_wrong_password(self):
        self.login_page.login(
            password=self.base_page.create_random_str()
        )
        login_error_page = LoginErrorPage(self.driver)
        assert login_error_page.find(login_error_page.locators.ERROR_MESSAGE_LOCATOR).is_displayed()

    @allure.epic('All tests')
    @allure.feature('UI test')
    @allure.story('Test wrong user name')
    @allure.description("""Negative test with wrong user name""")
    @pytest.mark.UI
    def test_wrong_user_name(self):
        self.login_page.login(
            user_name=self.base_page.create_random_str() +
                      '@' +
                      self.base_page.create_random_str() +
                      '.ru'
        )
        login_error_page = LoginErrorPage(self.driver)
        assert login_error_page.find(login_error_page.locators.ERROR_MESSAGE_LOCATOR).is_displayed()

    @allure.epic('All tests')
    @allure.feature('UI test')
    @allure.story('Test create campaign')
    @allure.description("""Test for creating an advertising campaign of any type and check that it is created""")
    @pytest.mark.UI
    def test_create_campaign(self, main_page, repo_root):
        campaign_creation_page = main_page.click_create_campaign()

        self.logger.info('Creating new campaign')
        with allure.step('Creating new campaign'):
            campaign_name = campaign_creation_page.create_campaign(repo_root)
        assert main_page.find(main_page.locators.CAMPAIGN_NAME_TEMPLATE(campaign_name))

        self.logger.info(f'Deleting campaign {campaign_name}')
        with allure.step(f'Deleting campaign {campaign_name}'):
            main_page.delete_campaign(campaign_name)

    @allure.epic('All tests')
    @allure.feature('UI test')
    @allure.story('Test create segment')
    @allure.description("""Test to create a segment in audiences and check that the segment is created""")
    @pytest.mark.UI
    def test_create_segment(self, main_page):
        self.logger.info('Going to audiences_page')
        with allure.step('Going to audiences page'):
            audiences_page = main_page.go_to_audiences_page()

        self.logger.info('Creating new segment')
        with allure.step('Creating new segment'):
            segment_name = audiences_page.create_segment()

        assert audiences_page.find(audiences_page.locators.SEGMENT_IN_LIST_TEMPLATE(segment_name)).is_displayed()

        self.logger.info(f'Deleting segment {segment_name}')
        with allure.step(f'Deleting segment {segment_name}'):
            audiences_page.delete_segment(segment_name)

    @allure.epic('All tests')
    @allure.feature('UI test')
    @allure.story('Test delete segment')
    @allure.description("""Test to delete a segment in audiences and check that the segment is deleted""")
    @pytest.mark.UI
    def test_delete_segment(self, main_page):
        self.logger.info('Going to audiences_page')
        with allure.step('Going to audiences page'):
            audiences_page = main_page.go_to_audiences_page()

        self.logger.info('Creating new segment')
        with allure.step('Creating new segment'):
            segment_name = audiences_page.create_segment()

        self.logger.info(f'Deleting segment {segment_name}')
        with allure.step(f'Deleting segment {segment_name}'):
            audiences_page.delete_segment(segment_name)

        assert audiences_page.is_segment_deleted(segment_name)
