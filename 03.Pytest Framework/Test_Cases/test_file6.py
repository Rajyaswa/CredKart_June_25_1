import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class Test005:

    @pytest.mark.sanity
    @pytest.mark.web
    def test_CredKart_Title_005(self, driver_setup):
        #driver = webdriver.Firefox()
        self.driver = driver_setup
        self.driver.get("https://automation.credence.in/login")
        print(f"Driver title is: {self.driver.title}")
        assert self.driver.title == "CredKart", "Title not matched"
        #driver.close()
