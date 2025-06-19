import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://apps.credence.in/practice/")
browser.maximize_window()

# Select Radio Button 2
time.sleep(2)
radio_button_2 = browser.find_element(By.XPATH, "//input[@value='radio2']")
radio_button_2.click()
time.sleep(2)

# Select Radio Button 1
time.sleep(2)
radio_button_1 = browser.find_element(By.XPATH, "//input[@value='radio1']")
radio_button_1.click()
time.sleep(2)

# Select Radio Button 3
time.sleep(2)
radio_button_3 = browser.find_element(By.XPATH, "//input[@value='radio3']")
radio_button_3.click()
time.sleep(2)

# Verify that the radio button 3 is selected
 # assert syntax: assert condition
 # Assert True --> Pass
 # Assert False --> Fail

#print("Radio Button 3 is selected:", radio_button_3.is_selected()) # True
assert radio_button_3.is_selected(), "Radio Button 3 is not selected"

browser.quit()