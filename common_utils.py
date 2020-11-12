from appium import webdriver
import os
import config

def set_up(self):
    desired_capabilities = {}
    desired_capabilities['platformName'] = config.capabilities["platformName"]
    desired_capabilities['platformVersion'] = config.capabilities["platformVersion"]
    desired_capabilities['deviceName'] = config.capabilities["deviceName"]
    desired_capabilities['udid'] = config.capabilities["udid"]
    desired_capabilities['app'] = os.path.abspath(config.capabilities["app"])
    self.driver = webdriver.Remote(config.capabilities["host"], desired_capabilities)

def tear_down(self):
    self.driver.quit()

def login (self, user_name, password):
    username_field = self.driver.find_element_by_accessibility_id('test-Username')
    password_field = self.driver.find_element_by_accessibility_id('test-Password')
    login_button = self.driver.find_element_by_accessibility_id('test-LOGIN')
    
    username_field.send_keys(user_name)
    password_field.send_keys(password)
    login_button.click()

def fill_payment_information (self, first_name, last_name, zip_code):
    first_name_field = self.driver.find_element_by_accessibility_id('test-First Name')
    last_name_field = self.driver.find_element_by_accessibility_id('test-Last Name')
    zip_code_field = self.driver.find_element_by_accessibility_id('test-Zip/Postal Code')
    continue_button = self.driver.find_element_by_accessibility_id('test-CONTINUE')
    
    first_name_field.send_keys(first_name)
    last_name_field.send_keys(last_name)
    zip_code_field.send_keys(zip_code)
    continue_button.click()