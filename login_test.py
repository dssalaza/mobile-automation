import unittest
import config
from common_utils import set_up, tear_down, login

class LoginTest(unittest.TestCase):
    test_name = 'Users can login'
    driver = None

    def test_locked_out_user_can_login (self):
        username = config.users["locked"]
        password = config.users["password"]
        set_up(self)
        
        login(self, username, password)
        hamburger_menu = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="test-Menu"]/XCUIElementTypeOther')
        hamburger_menu.click()
        logout_button = self.driver.find_element_by_accessibility_id('test-LOGOUT')
        
        assert logout_button.text == 'LOGOUT'
        tear_down(self)

    def test_problem_user_can_login (self):
        username = config.users["problem"]
        password = config.users["password"]
        set_up(self)
        
        login(self, username, password)
        hamburger_menu = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="test-Menu"]/XCUIElementTypeOther')
        hamburger_menu.click()
        logout_button = self.driver.find_element_by_accessibility_id('test-LOGOUT')
        
        assert logout_button.text == 'LOGOUT'
        tear_down(self)

    def test_standard_user_can_login (self):
        username = config.users["standard"]
        password = config.users["password"]
        set_up(self)
        
        login(self, username, password)
        hamburger_menu = self.driver.find_element_by_xpath('//XCUIElementTypeOther[@name="test-Menu"]/XCUIElementTypeOther')
        hamburger_menu.click()
        logout_button = self.driver.find_element_by_accessibility_id('test-LOGOUT')
        
        assert logout_button.text == 'LOGOUT'
        tear_down(self)