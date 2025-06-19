import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_BankApp_Login_Params:
    #@pytest.mark.flaky(reruns=5, reruns_delay=1)  # to retry the failed testcases
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



import pytest
from selenium import webdriver


@pytest.fixture # decorator
def demo_fixture(): # function
    print("\nThis is demo fixture, this will run first, before testcase") # Code # function body/ block
    # if you are using this fixture in any testcase then it will run before that testcase
    yield # after running the testcase this will run
    print("\nThis is demo fixture, this will run after testcase")


    '''
    browser open--> before testcase
    browser close--> after testcase
    '''

# @pytest.fixture
# def driver_setup():
#     print("\nBrowser opened")
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#     print("\nBrowser closed")


'''
pytest_addoption -- > hook up function --> extending pytest framework
Python adoption function is used to pass the command line arguments to pytest
here we are going to add "--browser" command line argument, which is user defined or custom argument.
( -v, -s, -m, -n --> predefined arguments) 
'''


def pytest_addoption(parser):
    parser.addoption("--browser")
# here we are going to add "--browser" command line argument, which is user defined or custom argument.

# --browser chrome
# --browser firefox
# --browser edge


@pytest.fixture
def driver_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("launching chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("launching firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("launching edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
         print("launching chrome headless browser")
         chrome_options = webdriver.ChromeOptions()
         chrome_options.add_argument("--headless")
         driver = webdriver.Chrome(options=chrome_options)
    else:
        #driver = webdriver.Chrome()
        print("launching chrome headless browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    print("\nBrowser closed")
    driver.quit()


def pytest_metadata(metadata):
    # To add metadata
    metadata["Project Name"] = "CredKart"
    metadata["Module Name"] = "Login"
    metadata["Tester Name"] = "Credence"
    metadata["URL"] = "https://apps.credence.in/"
    # To remove metadata
    del metadata["Platform"]

    # edit summary in html report --> your task

@pytest.fixture(params=[
    ("credence123111", "Credence@123987211", "Pass"),
    ("credence123111a", "Credence@123987211", "Fail"),
    ("credence123111", "Credence@123987211a",  "Fail"),
    ("credence123111a", "Credence@123987211a", "Pass")
])
def bankapp_login_data(request): # function with parameter
    return request.param



