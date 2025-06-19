import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
time.sleep(1)
dropdown_list = Select(driver.find_element(By.ID, "multiSelect"))
time.sleep(1)
dropdown_list.select_by_visible_text("Item 2")
time.sleep(1)
dropdown_list.select_by_visible_text("Item 3")
time.sleep(1)
dropdown_list.select_by_index(3)
time.sleep(2)