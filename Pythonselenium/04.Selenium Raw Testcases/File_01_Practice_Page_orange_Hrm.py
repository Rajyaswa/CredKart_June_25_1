import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
if driver.title == "OrangeHRM":
    print("you are landed on correct page and it's title is:", driver.title)
    # Find input fields (not labels)
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("Admin")
    time.sleep(3)
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")
    time.sleep(2)
# Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(1)
# Go To dashboard
    symbol=driver.find_element(By.XPATH, "//img[@alt='profile picture']").click()
    time.sleep(1)
# Click the Logout Button
    logout_button = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a").click()
    time.sleep(3)
    if driver.title == "OrangeHRM":
        print("you are logged successfully:", driver.title)
    else:
        print("you are not correctly logged out:",driver.title)
else:
    print("you are landed on wrong page and it's title is:", driver.title)
driver.quit()