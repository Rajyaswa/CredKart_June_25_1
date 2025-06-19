from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # ✅ Correct one

# Setup Edge driver
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

# Use browser
driver.maximize_window()
driver.get("https://credence.in/")
print("Page title:", driver.title)

driver.quit()
