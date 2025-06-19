from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Set the correct path to geckodriver
driver_path = r"C:\Users\SMAK\PycharmProjects\drivers\geckodriver.exe"

# Set up Firefox driver
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

# Open a test website
driver.get("https://www.google.com")

# Wait 5 seconds
driver.implicitly_wait(5)

# Close browser
driver.quit()
