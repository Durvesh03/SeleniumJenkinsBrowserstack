from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium import webdriver

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def EnterVal(self,by_locator,value):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(value)

    def do_click(self,by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def getText(self,by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def getattrval(self,by_locator,propName):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).get_attribute(propName)