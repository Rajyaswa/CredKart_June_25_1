import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()

# Open Tab 1
time.sleep(3)
open_window = driver.find_element(By.ID, "opentab1")
open_window.click()
time.sleep(2)
print(f"driver title : {driver.title}") # Practica Page
time.sleep(2)



# Switch To Tab 2 Credence
driver.switch_to.window(driver.window_handles[1]) # driver will switch to new window --> credence.in

print(f"driver title : {driver.title}") # Credence
time.sleep(3)

print(driver.find_element(By.CLASS_NAME, "text-white").text)
time.sleep(3)



# Switch Back to practice page
driver.switch_to.window(driver.window_handles[0])
print(f"driver title : {driver.title}") # Credence
time.sleep(3)


# Open 3rd tab of bank app site
driver.find_element(By.ID, "opentab2").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
print(f"driver title : {driver.title}") # Google

print(driver.find_element(By.XPATH, "/html/body/div/h2").text)


# Close Credence Site Tab
driver.switch_to.window(driver.window_handles[2])
driver.close()

# Close Practice page
driver.switch_to.window(driver.window_handles[0])
driver.close() # to close specific tab

driver.quit() # Close the browser and ending webdriver session

# close vs quit


