import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utils.Excel_utilities import Excel_utils


class Test_BankApp_SignUp_DDT:
    excel_file_path=r"C:\Users\SMAK\PycharmProjects\03.Pytest Framework\Tets_Data\Bank_App_Test_Data2.xlsx"
    sheet_name="SignUp"

    def test_bankapp_SignUp_DDT_003(self, driver_setup):
        driver = driver_setup
        driver.get("https://apps.credence.in/login.html")
        driver.maximize_window()
        print("Title of the page:", driver.title)
        sign_up = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="signUpLink"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", sign_up)
        sign_up.click()

        time.sleep(1)

        rows = Excel_utils.get_row_count(self.excel_file_path, self.sheet_name)
        print("Total rows are:", rows)
        Result_List = []
        for r in range(2, rows+1):

            username = Excel_utils.read_data_from_excel(self.excel_file_path, self.sheet_name, r, 2)
            password = Excel_utils.read_data_from_excel(self.excel_file_path, self.sheet_name, r, 3)
            email=Excel_utils.read_data_from_excel(self.excel_file_path,self.sheet_name,r,4)
            phone=Excel_utils.read_data_from_excel(self.excel_file_path,self.sheet_name,r,5)
            expected_result = Excel_utils.read_data_from_excel(self.excel_file_path, self.sheet_name, r, 6)

            print(f"Username is: {username}")
            print(f"Password is: {password}")
            print(f"email is :{email}")
            print(f"phone is :{phone}")
            print(f"Expected Result is: {expected_result}")

            # Enter Username
            #time.sleep(3)
            username_field = driver.find_element(By.ID, "username")
            username_field.send_keys(username)

            # Enter Password
            password_field = driver.find_element(By.NAME, "password")
            password_field.send_keys(password)

            #Email field
            email_field = driver.find_element(By.NAME,"email")
            email_field.send_keys(email)

            #Phone Field
            phone_field = driver.find_element(By.NAME,"phone")
            phone_field.send_keys(phone)

            # Click on Create User Button

            create_user_button = driver.find_element(By.ID, "createUserButton")
            driver.execute_script("arguments[0].scrollIntoView();", create_user_button )
            create_user_button .click()


            # Verify the User login Successfully
            wait = WebDriverWait(driver, 3)
            try:
                wait.until(
                    expected_conditions.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Dashboard']"))
                    )
                driver.find_element(By.XPATH, "//h2[normalize-space()='Dashboard']")
                print("User login Successfully")
                # driver.save_screenshot("User login Successfully.png")
                actual_result = "Pass"
                Excel_utils.write_data_to_excel(self.excel_file_path, self.sheet_name, r, 7, actual_result)
                #time.sleep(3)


                logout_button = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
                driver.execute_script("arguments[0].scrollIntoView();", logout_button)
                logout_button.click()
            except:
                print("User login Failed")
                # driver.save_screenshot("User login Failed.png")
                actual_result = "Fail"
                Excel_utils.write_data_to_excel(self.excel_file_path, self.sheet_name, r, 7, actual_result)

            if actual_result == expected_result:
                test_case_result = "Pass"
                print(f"Test Case Result is: {test_case_result}")
            else:
                test_case_result = "Fail"
                print(f"Test Case Result is: {test_case_result}")

            Excel_utils.write_data_to_excel(self.excel_file_path, self.sheet_name, r, 8, test_case_result)
            Result_List.append(test_case_result)

        print(f"Result List is: {Result_List}")
        assert "Fail" not in Result_List, "Test Case Failed"
        # if "Fail" not in Result_List:
        #     assert True
        # else:
        #     assert False