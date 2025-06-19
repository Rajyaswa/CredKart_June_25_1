from selenium import webdriver
from selenium.webdriver.edge.service import Service

# ✅ Path to your Edge WebDriver
driver_path = r"C:\Users\SMAK\PycharmProjects\Pythonselenium\drivers\msedgedriver.exe"

service = Service(driver_path)
driver = webdriver.Edge(service=service)

driver.maximize_window()
driver.get("https://www.google.com")

print("Title:", driver.title)

driver.quit()
