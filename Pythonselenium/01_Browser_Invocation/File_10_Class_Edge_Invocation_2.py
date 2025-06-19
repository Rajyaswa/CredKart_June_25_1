from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Path to your manually downloaded Edge driver
driver_path = r"C:\Users\SMAK\PycharmProjects\Pythonselenium\drivers\msedgedriver.exe"
service = Service(driver_path)

driver = webdriver.Edge(service=service)
driver.maximize_window()
driver.get("https://credence.in/")

print("Page title:", driver.title)

driver.quit()
