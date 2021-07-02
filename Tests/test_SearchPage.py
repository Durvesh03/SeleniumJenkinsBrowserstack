import time

import pytest
from selenium import webdriver

from Pages.SearchPage import SearchPage
from Tests.test_BaseClass import BaseTest


class Test_SearchPage(BaseTest):

    def test_searchResults(self):
        self.sp = SearchPage(self.driver)
        self.sp.EnterSearchVal("Samsung Galaxy S10")
        self.sp.clickMobile()
        self.sp.SelectSamsung()
        self.sp.SelectFAssure()
        self.sp.SelectHighToLow()
        time.sleep(5)
        print(self.sp.PrintSearchedItems())


