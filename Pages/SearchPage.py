import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Config.Config import TestData
from Pages.BasePage import BasePage


class SearchPage(BasePage):
    SEARCH_BOX = (By.XPATH,"//input[@name='q']")
    SEARCH_BUTTON = (By.XPATH,"//button[@class='L0Z3Pu']")
    MOBILES_LABEL = (By.XPATH,"(//span[contains(text(),'CATEGORIES')]/parent::div/following-sibling::div)[2]/div/a")
    SAMSUNG_CHECKBOX = (By.XPATH,"//div[@title='SAMSUNG']/div/label/div")
    # F_ASSURED_CHECKBOX = (By.XPATH,"//span[@class='question']/parent::div/parent::section/label/input")
    F_ASSURED_CHECKBOX = (By.XPATH,"//span[@class='question']/parent::div/parent::section/label/div/div/img")
    HIGH_TO_LOW_FILTER = (By.XPATH,"//div[contains(text(),'High to Low')]")
    CLOSE_BUTTON = (By.XPATH,"//button[@class='_2KpZ6l _2doB4z']")
    SEARCHED_ITEMS_XPATH = "//div[contains(text(),'SAMSUNG ')]"
    SEARCHED_ITEMS = (By.XPATH,SEARCHED_ITEMS_XPATH)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def EnterSearchVal(self,value):
        self.do_click(self.CLOSE_BUTTON)
        self.do_click(self.SEARCH_BOX)
        self.EnterVal(self.SEARCH_BOX,value)
        self.do_click(self.SEARCH_BUTTON)

    def clickMobile(self):
        self.do_click(self.MOBILES_LABEL)

    def SelectSamsung(self):
        self.do_click(self.SAMSUNG_CHECKBOX)

    def SelectFAssure(self):
        self.do_click(self.F_ASSURED_CHECKBOX)

    def SelectHighToLow(self):
        self.do_click(self.HIGH_TO_LOW_FILTER)

    def PrintSearchedItems(self):
        result = ""
        Total_items = len(self.driver.find_elements_by_xpath(self.SEARCHED_ITEMS_XPATH))
        for i in range(1,Total_items+1):
            item_name_xpath = "(" + self.SEARCHED_ITEMS_XPATH + ")[" + str(i) + "]"
            item_name = self.getText((By.XPATH,item_name_xpath))

            item_value_xpath = item_name_xpath + "/parent::div/following-sibling::div/div/div/div"
            item_value = self.getText((By.XPATH, item_value_xpath))
            item_link_xpath = item_name_xpath + "/parent::div/parent::div/parent::a"
            item_link = self.getattrval((By.XPATH, item_link_xpath),'href')
            result = result + item_name + "|" + item_value +  "|" + item_link + "/n"

        return result
