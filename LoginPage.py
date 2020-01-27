from selenium import webdriver


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def login_as(self, username, password):
        self.driver.find_element_by_id("user-name").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_css_selector(".btn_action").click()

    def is_error_present(self):
        return len(self.driver.find_elements_by_css_selector('.error-button'))
