# This is your task
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://apps.credence.in/practice/")
browser.maximize_window()

# Select Text Box Example
time.sleep(2)
Text_Box_Example = browser.find_element(By.XPATH, "//input[@id='autocomplete']")
Text_Box_Example.click()
Text_Box_Example.send_keys("Credence123")
time.sleep(2)