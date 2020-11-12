import unittest
import config
from common_utils import *

class LoginTest(unittest.TestCase):
    test_name = 'Users can login'
    driver = None

    def test_standard_user_checkout (self):
        max_swipes = 4
        username = config.users["standard"]
        password = config.users["password"]
        firstname = config.payment_info["firstName"]
        lastname = config.payment_info["lastName"]
        zipcode = config.payment_info["zipCode"]

        set_up(self)
        
        login(self, username, password)

        for x in range(1, max_swipes, 1):
            try:
                if self.driver.find_element_by_ios_predicate('label == "Sauce Labs Onesie"'):
                    item = self.driver.find_element_by_ios_predicate('label == "Sauce Labs Onesie"')
                    item.click()
                    break
            except:
                self.driver.execute_script("mobile: swipe", {'direction': 'up'})

        for y in range(1, max_swipes, 1):
            try:
                if self.driver.find_element_by_accessibility_id('test-ADD TO CART'):
                    add_to_cart_button = self.driver.find_element_by_accessibility_id('test-ADD TO CART')
                    add_to_cart_button.click()
                    break
            except:
                self.driver.execute_script("mobile: swipe", {'direction': 'up'})
        
        cart_button = self.driver.find_element_by_ios_class_chain('**/XCUIElementTypeOther[`name == "test-Cart"`]/XCUIElementTypeOther')
        cart_button.click()

        checkout_button = self.driver.find_element_by_accessibility_id('test-CHECKOUT')
        checkout_button.click()

        fill_payment_information(self, firstname, lastname, zipcode)

        for z in range(1, max_swipes, 1):
            try:
                if self.driver.find_element_by_accessibility_id('test-FINISH'):
                    finish_button = self.driver.find_element_by_accessibility_id('test-FINISH')
                    finish_button.click()
                    break
            except:
                self.driver.execute_script("mobile: swipe", {'direction': 'up'})

        thank_you_label = self.driver.find_element_by_accessibility_id('THANK YOU FOR YOU ORDER')
        
        assert thank_you_label.text == 'THANK YOU FOR YOU ORDER'
