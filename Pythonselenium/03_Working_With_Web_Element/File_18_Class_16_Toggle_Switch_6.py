import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
time.sleep(1)
from selenium.webdriver.common.by import By

# Click the label, not the input
driver.find_element(By.CSS_SELECTOR, "label[for='male']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "label[for='female']").click()
time.sleep(2)

