import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://automation.credence.in/register")
driver.maximize_window()

value = "011"

if driver.title == "CredKart":
    print("you are landed on correct page and it's title is:", driver.title)
    # Field - Name
    name_field = driver.find_element(By.ID, "name")
    name_field.send_keys(f"Credencejune{value}")

    # Field - Email
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys(f"Credencejune{value}@credence.in")

    # Field - Password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Credence@123")

    # Field - Confirm Password
    confirm_password_field = driver.find_element(By.ID, "password-confirm")
    confirm_password_field.send_keys("Credence@123")

    # Button - Register Now
    register_now_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    register_now_button.click()

    # Verify the User Registered Successfully
    wait = WebDriverWait(driver, 5)
    try :
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
        driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
        print("User Registered Successfully")
        driver.save_screenshot("User Registered Successfully.png")
    except :
        print("User Registration Failed")
        driver.save_screenshot("User Registered Failed.png")
else:
    print("you are landed on wrong page and it's title is:", driver.title)


driver.quit()

"""
Selector Hub Url :
https://addons.mozilla.org/en-US/firefox/addon/selectorshub/

# Add to Firefox


https://chromewebstore.google.com/detail/selectorshub/ndgimibanhlabgdgjcpbbndiehljcpfh

# Add to Chrome



TestCase Studio :

https://addons.mozilla.org/en-US/firefox/addon/testcase-studio/

# Add to Firefox

"""


