from simplesauce.session import SauceSession


BASE_TEST_URL = 'https://www.saucedemo.com'


class SauceLabs(object):

    def __init__(self):
        self.sauce = {}

    def start_session(self):
        self.sauce = SauceSession()
        self.sauce.start()

    def go_to_demo(self):
        self.sauce.driver.get(BASE_TEST_URL)
    
    def title_is_correct(self):
        assert "Swag" in self.sauce.driver.title

    def stop_session(self):
        self.sauce.stop(True)
