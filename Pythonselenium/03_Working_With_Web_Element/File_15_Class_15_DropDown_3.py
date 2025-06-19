import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://apps.credence.in/practice")

driver.maximize_window()

# Select DropDown
time.sleep(2)

dropdown = driver.find_element(By.ID, "dropdown-class-example")

# Scroll
# driver.execute_script("arguments[0].scrollIntoView();", dropdown) # java script

select_dropdown = Select(dropdown)
select_dropdown.select_by_visible_text("Option3")

time.sleep(2)
select_dropdown.select_by_index(2)



assert select_dropdown.first_selected_option.text =="Option1", "DropDown Option 1 is not selected"
time.sleep(5)
driver.quit()
