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
username_field.send_keys("credence")
time.sleep(2)

# Enter Password
# driver.find_element(By.NAME, "password").send_keys("credence")
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Credence@123")
time.sleep(2)

# Enter Email

email_field = driver.find_element(By.CLASS_NAME, "email")
email_field.send_keys("credence12343@gmail.com")
time.sleep(2)
driver.quit()

# Enter Phone
Input_field= driver.find_elements(By.TAG_NAME, "input")
phone_field = Input_field[3]
phone_field.send_keys("1234567660")
time.sleep(2)