from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.NAME, 'email')
    CONTINUE_BUTTON = (By.CLASS_NAME, 'a-button-input')
    PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.ID, 'auth-signin-button')

    def fill_email_text_box(self, email_text):
        self.send_text(email_text, *self.EMAIL)

    def click_continue_button(self):
        self.click_element(*self.CONTINUE_BUTTON)

    def fill_password_text_box(self, password_text):
        self.send_text(password_text, *self.PASSWORD)

    def click_login2_button(self):
        self.click_element(*self.LOGIN_BUTTON)
