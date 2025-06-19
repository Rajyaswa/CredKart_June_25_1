from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# ✅ Give full path to geckodriver.exe
driver_path = r"C:\Users\SMAK\PycharmProjects\drivers\geckodriver.exe"
service = Service(driver_path)

# ✅ Launch Firefox using the driver manually
driver = webdriver.Firefox(service=service)

driver.get("https://credence.in/")
print("Title is:", driver.title)
driver.quit()


