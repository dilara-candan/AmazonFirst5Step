from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from test.base_test import BaseTest


class TestCheckAmazon(BaseTest):
    email_text = '5538660222'
    password_text = '590866'
    search_text = 'samsung'
    search_text_2 = '"samsung"'

    def test_check_amazon(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.is_present_homepage())
        home_page.click_login1()

        login_page = LoginPage(self.driver)
        login_page.fill_email_text_box(self.email_text)
        login_page.click_continue_button()
        login_page.fill_password_text_box(self.password_text)
        login_page.click_login2_button()

        home_page.fill_search_text_box(self.search_text)
        home_page.click_search_button()

        category_page = CategoryPage(self.driver)
        self.assertEqual(self.search_text_2, category_page.get_search_text())
        category_page.click_page()
        self.assertTrue(category_page.is_present_page2())

    def tear_down(self):
        self.driver.quit()