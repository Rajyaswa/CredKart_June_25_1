import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch browser
driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()
time.sleep(2)

# Locate the date input field by its ID
date_input = driver.find_element(By.ID, "datePicker")

# Clear the field (optional)
date_input.clear()

# Send the date in correct format
date_input.send_keys("07/02/2025")  # Format: MM/DD/YYYY

# Locate the time input field by its ID
time_input = driver.find_element(By.ID, "timePicker")

# Clear any existing value
time_input.clear()

# Enter time - format depends on the input type, commonly HH:MM (24-hour format)
time_input.send_keys("14:30")  # Example: 2:30 PM in 24-hour format
SUBMIT=driver.find_element(By.XPATH,("//*[@id='dateTimeBtn']")).click()

time.sleep(3)
driver.quit()
