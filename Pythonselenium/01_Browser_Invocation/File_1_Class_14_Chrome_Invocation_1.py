from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# ✅ Make sure this is the FULL path to chromedriver.exe
driver_path = r"C:\Users\SMAK\PycharmProjects\drivers\chromedriver.exe"

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
