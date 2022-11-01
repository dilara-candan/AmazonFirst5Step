from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):
    PAGE = (By.CSS_SELECTOR, '[aria-label="Go to page 2"]')
    PAGE2 = (By.CSS_SELECTOR, '[aria-label="Current page, page 2"]')
    SEARCH_TEXT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')

    def click_page(self):
        self.click_element(*self.PAGE)

    def is_present_page2(self):
        return self.find_element(*self.PAGE2)

    def get_search_text(self):
        return self.find_element(*self.SEARCH_TEXT).text
