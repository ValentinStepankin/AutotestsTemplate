import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class UserSettingsPage(BasePage):

    PAGE_URL = Links.SETTINGS

    FIRSTNAME_FIELD = ('id', 'name')
    SAVE_BUTTON = ('data-test', 'save-settings')

    def change_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRSTNAME_FIELD))
            first_name_field.clear()
            assert first_name_field.get_attribute('value') == '', 'There is text'
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step('Click save button')
    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step('Changes saved successfully')
    def is_changes_saved(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRSTNAME_FIELD, self.name))

