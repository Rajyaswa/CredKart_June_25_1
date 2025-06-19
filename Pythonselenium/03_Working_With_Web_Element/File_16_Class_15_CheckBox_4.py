import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://apps.credence.in/practice/")
browser.maximize_window()

# Select Radio Button 2
time.sleep(2)
Checkbox_Example = browser.find_element(By.XPATH, "//input[@value='option2']")
Checkbox_Example.click()
time.sleep(2)

# Select Radio Button 1
Checkbox_Example = browser.find_element(By.XPATH, "//input[@value='option1']")
Checkbox_Example.click()
time.sleep(2)

time.sleep(2)
Checkbox_Example = browser.find_element(By.XPATH, "//input[@value='option3']")
Checkbox_Example.click()
time.sleep(2)