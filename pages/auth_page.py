import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AuthPage(BasePage):

    PAGE_URL = Links.AUTH_PAGE

    EMAIL_FIELD = ('id', 'email')
    PASSWORD_FIELD = ('id', 'password')
    SUBMIT_BUTTON = ('xpath', "//*[@data-test='enter']")


    @allure.step('Enter login')
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(login)

    @allure.step('Enter password')
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step('Click submit button')
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()