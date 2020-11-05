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