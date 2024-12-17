import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):

    PAGE_URL = Links.HOST

    PROFILE_ICON = ('data-test', 'profile-menu')
    PROFILE_WINDOW_SETTINGS = ('data-test', 'settings')

    @allure.step('Click profile icon')
    def click_profile_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_ICON)).click()

    @allure.step('Hover over profile icon')
    def hover_profile_icon(self):
        actions = ActionChains(self.driver)
        profile_menu_element = self.wait.until(EC.visibility_of_element_located(self.PROFILE_ICON))
        actions.move_to_element(profile_menu_element).perform()

    @allure.step('Click settings in the profile window')
    def click_settings_in_profile_window(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_WINDOW_SETTINGS)).click()