import time
from selenium import webdriver # Import selenium module
from selenium.webdriver.firefox.service import Service # Import Service
from webdriver_manager.firefox import GeckoDriverManager # Import ChromeDriverManager #1
service = Service(GeckoDriverManager().install()) #2
driver = webdriver.Firefox(service=service) #
driver.maximize_window()
driver.get("https://credence.in/") # Open credence website
print("Title of the page:", driver.title) # Print title of the page # Credence
time.sleep(5)
driver.quit()