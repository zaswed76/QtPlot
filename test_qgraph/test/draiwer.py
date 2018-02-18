
from selenium import webdriver
import requests

class SeleniumCBT():
    def __init__(self):
        self.setUp()
    def setUp(self):

        self.username = "zaswed"
        self.authkey  = "fasadAQ9"

        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)
        self.test_result = None

        caps = {}
        caps['browserName'] = 'Chrome'
        caps['version'] = '60x64'
        caps['platform'] = 'Windows 7'
        caps['screenResolution'] = '1366x768'

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey)
        )

        self.driver.implicitly_wait(20)

    def test(self):
            self.driver.get('http://adminold.itland.enes.tech/index.php/map')

            self.test_result = 'pass'
            self.driver.quit()


if __name__ == '__main__':
    m = SeleniumCBT()
    m.test()