import time
from selenium import webdriver # Import selenium module
from selenium.webdriver.chrome.service import Service # Import Service
from webdriver_manager.chrome import ChromeDriverManager # Import ChromeDriverManager #1
service = Service(ChromeDriverManager().install()) #2
driver = webdriver.Chrome(service=service) #
driver.maximize_window()
driver.get("https://credence.in/") # Open credence website
print("Title of the page:", driver.title) # Print title of the page # Credence
time.sleep(5)
driver.quit() # Close the browser and ending webdriver session
