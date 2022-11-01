from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    HOMEPAGE_CONTROL = (By.CSS_SELECTOR, '.gw-desktop-herotator')
    LOGIN_1 = (By.CSS_SELECTOR, '.nav-line-1-container')
    SEARCH = (By.NAME, 'field-keywords')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')

    def click_login1(self):
        self.click_element(*self.LOGIN_1)

    def fill_search_text_box(self, search_text):
        self.send_text(search_text, *self.SEARCH)

    def click_search_button(self):
        self.click_element(*self.SEARCH_BUTTON)

    def is_present_homepage(self):
        return self.find_element(*self.HOMEPAGE_CONTROL)
