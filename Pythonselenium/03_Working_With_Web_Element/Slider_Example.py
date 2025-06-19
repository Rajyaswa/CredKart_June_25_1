import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://apps.credence.in/practice/")
browser.maximize_window()

# Select Radio Button 2
time.sleep(8)
Slider_Example = browser.find_element(By.XPATH, "//input[@min='0']")
Slider_Example.click()
time.sleep(8)



