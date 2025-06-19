import time

from selenium import webdriver # Import selenium module

driver = webdriver.Chrome() # Chrome driver object just to invoke chrome browser
driver.maximize_window()
driver.get("https://credence.in/") # Open credence website
print("Title of the page:", driver.title) # Print title of the page # Credence
time.sleep(5)
driver.quit() # Close the browser and ending webdriver session
