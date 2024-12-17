import pytest

from config.data import Data
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.user_settings_page import UserSettingsPage

class BaseTest:

    data: Data

    auth_page: AuthPage
    main_page: MainPage
    user_settings_page: UserSettingsPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.auth_page = AuthPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.user_settings_page = UserSettingsPage(driver)