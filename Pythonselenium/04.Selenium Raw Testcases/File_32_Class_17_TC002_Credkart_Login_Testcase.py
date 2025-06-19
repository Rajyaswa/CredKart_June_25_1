import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://automation.credence.in/login")
driver.maximize_window()

value = "09"

if driver.title == "CredKart":
    print("you are landed on correct page and it's title is:", driver.title)

    # Field - Email
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys(f"Credencejune{value}@credence.in")

    # Field - Password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Credence@123")

    # Button - Login Now
    login_now_button = driver.find_element(By.CLASS_NAME, "btn")
    login_now_button.click()

    # Verify the User login Successfully
    wait = WebDriverWait(driver, 5)
    try :
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
        driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
        print("User login Successfully")
        driver.save_screenshot("User login Successfully.png")
    except :
        print("User login Failed")
        driver.save_screenshot("User login Failed.png")
else:
    print("you are landed on wrong page and it's title is:", driver.title)


driver.quit()


