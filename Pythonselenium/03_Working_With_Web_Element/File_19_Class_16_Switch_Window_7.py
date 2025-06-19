import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
open_window = driver.find_element(By.ID, "openwindow")
open_window.click()
time.sleep(2)
print(f"driver title : {driver.title}") # Practica Page
time.sleep(2)
# Switch To window
driver.switch_to.window(driver.window_handles[1]) # driver will switch to new window --> credence.in

print(f"driver title : {driver.title}") # Credence
time.sleep(2)

print(driver.find_element(By.CLASS_NAME, "text-white").text)

# Switch Back to practice page
driver.switch_to.window(driver.window_handles[0])
print(f"driver title : {driver.title}") # Credence