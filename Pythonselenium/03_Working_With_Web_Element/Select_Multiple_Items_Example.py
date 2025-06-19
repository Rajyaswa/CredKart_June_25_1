import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://apps.credence.in/practice/")
browser.maximize_window()

# Select Radio Button 2
time.sleep(2)
Select_Multiple_Items_Example = browser.find_element(By.XPATH, "//option[@value='item1']")
Select_Multiple_Items_Example.click()
time.sleep(2)

# Select Radio Button 1
Select_Multiple_Items_Example = browser.find_element(By.XPATH, "//option[@value='item2']")
Select_Multiple_Items_Example.click()
time.sleep(2)

time.sleep(2)
Select_Multiple_Items_Example = browser.find_element(By.XPATH, "//option[@value='item3']")
Select_Multiple_Items_Example.click()
time.sleep(2)

time.sleep(2)
Select_Multiple_Items_Example = browser.find_element(By.XPATH, "//option[@value='item4']")
Select_Multiple_Items_Example.click()
time.sleep(2)

time.sleep(2)
Select_Multiple_Items_Example = browser.find_element(By.XPATH, "//option[@value='item5']")
Select_Multiple_Items_Example.click()
time.sleep(2)

browser.quit()