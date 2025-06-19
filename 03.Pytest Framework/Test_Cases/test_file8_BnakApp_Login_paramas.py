import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_BankApp_Login_Params:
    @pytest.mark.flaky(reruns=5, reruns_delay=1)  # to retry the failed testcases
    def test_bankapp_login_params_002(self, driver_setup, bankapp_login_data):

        username = bankapp_login_data[0]
        password = bankapp_login_data[1]
        expected_result = bankapp_login_data[2]
        print(f"Username is: {username}")
        print(f"Password is: {password}")
        print(f"Expected Result is: {expected_result}")

        driver = driver_setup
        driver.get("https://apps.credence.in/login.html")
        driver.maximize_window()
        # time.sleep(2)
        print("Title of the page:", driver.title)

        # Enter Username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)

        # Enter Password
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(password)

        # Click on Create User Button

        login_button = driver.find_element(By.ID, "loginButton")
        login_button.click()
        # Verify the User login Successfully
        wait = WebDriverWait(driver, 5)
        try:
            wait.until(
                expected_conditions.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Dashboard']"))
                )
            driver.find_element(By.XPATH, "//h2[normalize-space()='Dashboard']")
            print("User login Successfully")
            # driver.save_screenshot("User login Successfully.png")
            actual_result = "Pass"
        except:
            print("User login Failed")
            # driver.save_screenshot("User login Failed.png")
            actual_result = "Fail"

        assert actual_result == expected_result

        # if actual_result == expected_result:
        #     assert True
        # else:
        #     assert False



