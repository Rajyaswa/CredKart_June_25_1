from selenium import webdriver # Import selenium module
from selenium.webdriver.chrome.options import Options # Import Options
chrome_options = Options() # Create chrome options object
chrome_options.add_argument("--headless") # Add headless option

driver = webdriver.Chrome(options=chrome_options) # Chrome driver object just to invoke chrome browser

driver.get("https://credence.in/") # Open credence website
print("Title of the page:", driver.title) # Print title of the page # Credence

driver.quit()