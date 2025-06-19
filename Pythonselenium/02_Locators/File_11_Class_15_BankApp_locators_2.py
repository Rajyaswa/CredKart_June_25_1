'''

List of all locators available in Python selenium :
1. id
2. name
3. class_name
4. tag_name
5. link_text
6. partial_link_text
7. css_selector
8. xpath

'''


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/user.html")
driver.maximize_window()
#time.sleep(2)
print("Title of the page:", driver.title)

# Enter Username
# driver.find_element(By.ID, "username").send_keys("credence")

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("credence1231")
time.sleep(2)

# Enter Password
# driver.find_element(By.NAME, "password").send_keys("credence")
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Credence@1239872")
time.sleep(2)

# Enter Email

email_field = driver.find_element(By.CLASS_NAME, "email")
email_field.send_keys("credence12343@gmail.com")
time.sleep(2)


# Enter Phone
Input_field= driver.find_elements(By.TAG_NAME, "input")
phone_field = Input_field[3]
phone_field.send_keys("1234567660")
time.sleep(2)

'''
# Click on Create User Button

create_user_button = driver.find_element(By.ID, "createUserButton")
#create_user_button.click()


'''
# Click Login Link - Link Text
login_link = driver.find_element(By.LINK_TEXT, "Go to Login")
login_link.click()




# Click Login Link - Partial Link Text
login_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Login")
login_link.click()

time.sleep(10)

driver.quit()