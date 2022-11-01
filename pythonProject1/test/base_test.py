import unittest

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class BaseTest(unittest.TestCase):
    base_url = 'https://www.amazon.com/'

    def setUp(self):
        option = Options()
        option.add_argument('--start-maximized')
        option.add_argument('--disable-extensions')

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
