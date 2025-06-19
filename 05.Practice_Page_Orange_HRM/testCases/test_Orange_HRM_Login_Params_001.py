import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import allure
import pytest
from faker import Faker
from pageObjects.Registration_Page import Registration_Page_Class
from pageObjects.Login_Page import Login_Page_Class
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.ReadConfig import ReadConfigClass
from utilities.Logger import log_generator_class


@pytest.mark.usefixtures("driver_setup")
class Test_User_Profile_Class:
    driver = None
    login_url = ReadConfigClass.get_data_for_login_url()
    register_url = ReadConfigClass.get_data_for_register_url()
    log = log_generator_class.loggen_method()



    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("orangehrm login")
    @allure.story("story: orangehrm Login")
    @allure.description("This test case is to validate orangehrmLogin functionality")
    @allure.issue("issue : https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.testcase("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.epic("Epic : OrangeHRM")
    @allure.sub_suite("OrangeHRM Login")
    @allure.title("test_Orange_HRM_Login_001")
    @pytest.mark.sanity
    @pytest.mark.web
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_Orange_HRM_Login_params_002(self, get_data_for_login):
        self.log.info("Testcase test_CredKart_Login_002 is started")
        self.log.info(f"Opening browser and landing on login page--{self.login_url}")
        self.driver.get(self.login_url)
        self.lp = Login_Page_Class(self.driver)  # Object Creation

        self.username = get_data_for_login[0]
        self.password = get_data_for_login[1]
        self.expected_result = get_data_for_login[2]

        self.log.info(f"Entering username--{self.username}")
        self.lp.Enter_Username(self.username)
        self.log.info(f"Entering password")
        self.lp.Enter_Password(self.password)
        self.log.info("Clicking on login button")
        self.lp.Click_Login_Button()  # Correct method name
        self.log.info("Verifying user login")

        if self.lp.verify_menu() == "Pass":
            self.log.info("User login successful")
            self.lp.Click_Menu_Button()
            self.lp.Click_Logout_Link()
            actual_result = "Pass"
        else:
            self.log.info("User login failed")
            actual_result = "Fail"
            self.driver.save_screenshot(
                r"C:\Users\SMAK\PycharmProjects\04.CreadKart_Pytest_Framework\ScreenShot\User login Failed.png")

        assert actual_result == self.expected_result, f"Expected Result: {self.expected_result}, Actual Result: {actual_result}"
        self.log.info("Testcase test_CredKart_Login_002 is completed\n")

