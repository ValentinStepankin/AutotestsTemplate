import random
import time

import allure
import pytest
from base.base_test import BaseTest
from conftest import driver


@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title('Change profile name')
    @allure.severity('Critical')
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.auth_page.open()
        self.auth_page.enter_login(self.data.LOGIN)
        self.auth_page.enter_password(self.data.PASSWORD)
        self.auth_page.click_submit_button()
        # self.main_page.is_opened()
        time.sleep(20)
        self.main_page.hover_profile_icon()
        self.main_page.click_settings_in_profile_window()
        self.user_settings_page.is_opened()
        self.user_settings_page.change_name(f'Test {random.randint(1, 100)}')
        self.user_settings_page.click_save_button()
        self.user_settings_page.is_changes_saved()

