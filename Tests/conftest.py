import pytest
from selenium import webdriver

from Config.Config import TestData


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        request.cls.driver = web_driver
        web_driver.implicitly_wait(10)
        yield
        web_driver.quit()
