class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locators):
        return self.driver.find_element(*locators)

    def click_element(self, *locators):
        self.find_element(*locators).click()

    def send_text(self, text, *locators):
        self.find_element(*locators).send_keys(text)
