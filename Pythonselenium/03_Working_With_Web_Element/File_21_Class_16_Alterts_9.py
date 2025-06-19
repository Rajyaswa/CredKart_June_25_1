import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()


time.sleep(2)

# 01 Simple Alert
# Click on Simple Alert button
driver.find_element(By.ID, "simpleAlert").click()
alert  = Alert(driver)

# Get the text of the alert
print(alert.text)
time.sleep(2)

# Accept the alert
alert.accept()
time.sleep(2)



#####################################################################
# 02. Confirm Alert
# Click on Confirm Alert button
time.sleep(2)

driver.find_element(By.ID, "confirmAlert").click()
alert  = Alert(driver)
print(alert.text) # Do you confirm this action?
time.sleep(2)

# alert.accept()
alert.accept()
time.sleep(2)

 # You confirmed the action.
alert.accept() # ok

time.sleep(2)


# For Dismiss
driver.find_element(By.ID, "confirmAlert").click()
time.sleep(2)

# click on cancel button
alert.dismiss()
time.sleep(2)
print(alert.text)# You canceled the action.
time.sleep(2)

alert.accept() # ok


#################################

# 03 Prompt Alert
time.sleep(2)
driver.find_element(By.ID, "promptAlert").click()
alert  = Alert(driver)
print(alert.text) # Please enter your name
time.sleep(2)

alert.send_keys("Credence")
time.sleep(2)

alert.accept()

driver.quit()

