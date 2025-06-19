import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://apps.credence.in/practice")

driver.maximize_window()

# Mouse Hover

mouse_actions = ActionChains(driver)
mouse_hover_button =  driver.find_element(By.ID, "mousehover")

# Scroll to the element - Mouse Hover button
driver.execute_script("arguments[0].scrollIntoView();", mouse_hover_button)
time.sleep(2)
mouse_actions.move_to_element(mouse_hover_button).perform()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Top").click()
driver.save_screenshot("mouse_hover_Top.png") # put it in specific folder, your task
driver.quit()