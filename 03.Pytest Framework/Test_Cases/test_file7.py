import time

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
    def test_CredKart_Title_007(self, driver_setup): # fail
        #driver = webdriver.Firefox()
        self.driver = driver_setup
        self.driver.get("https://automation.credence.in/login")
        print(f"Driver title is: {self.driver.title}")
        assert self.driver.title == "CredKart1", "Title not matched" # given wrong title
        #driver.close()

    @pytest.mark.math
    @pytest.mark.sanity
    @pytest.mark.skip # to skip the testcases ( Intentionally we are not executing the test cases because there is a bug which is not yet resolve or the test case development is not fully completed as per requirement so intentionally we are skipping the test cases from run.
    def test_sum_001(self, demo_fixture): # skip
        print("Test001")
        a = 1
        b = 10
        sum = a + b
        print(f"Sum of {a} and {b} is {sum}")
        assert sum == 11  # pass



    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.xfail # expected to fail
    def test_sum_0010(self):
        print("Test002")
        a = 12
        b = 10
        sum = a + b
        print(f"Sum of {a} and {b} is {sum}")
        assert sum == 21 # fail

    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.xfail
    def test_mul_011(self):
        print("Test003")
        a = 12
        b = 10
        mul = a * b
        print(f"Mul of {a} and {b} is {mul}")
        assert mul == 120


    @pytest.mark.regression
    @pytest.mark.web
    def test_CredKart_Login_0010(self,
                                driver_setup):
        driver = driver_setup
        driver.get("https://automation.credence.in/login")
        driver.maximize_window()

        value = "0155"

        if driver.title == "CredKart":
            print("you are landed on correct page and it's title is:", driver.title)

            # Field - Email
            email_field = driver.find_element(By.ID, "email")
            email_field.send_keys(f"Credencejune{value}@credence.in")

            # Field - Password
            password_field = driver.find_element(By.ID, "password")
            password_field.send_keys("Credence@123")

            # Button - Login Now
            login_now_button = driver.find_element(By.CLASS_NAME, "btn") # given wrong class name
            login_now_button.click()

            # Verify the User login Successfully
            wait = WebDriverWait(driver, 5)
            try:
                wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
                driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
                print("User login Successfully")
                # driver.save_screenshot("User login Successfully.png")
            except:
                print("User login Failed")
                # driver.save_screenshot("User login Failed.png")
        else:
            print("you are landed on wrong page and it's title is:", driver.title)

    @pytest.mark.flaky(reruns = 5, reruns_delay = 1) # to retry the failed testcases
    def test_bankapp_login_001(self, driver_setup):
        driver = driver_setup
        driver.get("https://apps.credence.in/login.html")
        driver.maximize_window()
        # time.sleep(2)
        print("Title of the page:", driver.title)

        # Enter Username
        # driver.find_element(By.ID, "username").send_keys("credence")

        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("credence123111")


        # Enter Password
        # driver.find_element(By.NAME, "password").send_keys("credence")
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("Credence@123987211")



        # Click on Create User Button

        login_button = driver.find_element(By.ID, "loginButton")
        login_button.click()
        # Verify the User login Successfully
        wait = WebDriverWait(driver, 5)
        try:
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Dashboard']")))
            driver.find_element(By.XPATH, "//h2[normalize-space()='Dashboard']")
            print("User login Successfully")
            # driver.save_screenshot("User login Successfully.png")
            assert True
        except:
            print("User login Failed")
            # driver.save_screenshot("User login Failed.png")
            assert False