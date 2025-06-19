from selenium import webdriver # Import selenium module
from selenium.webdriver.firefox.options import Options # Import Options

firefox_options = Options() # Create chrome options object
firefox_options.add_argument("--headless") # Add headless option

driver = webdriver.Firefox(options=firefox_options) # Chrome driver object just to invoke chrome browser

driver.get("https://credence.in/") # Open credence website
print("Title of the page:", driver.title) # Print title of the page # Credence

driver.quit()