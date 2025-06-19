import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()

if driver.title == "nopCommerce demo store. Login":
    print("you are landed on correct page and it's title is:", driver.title)
#email field
    email=driver.find_element(By.NAME,"Email")
    email.send_keys("")
    time.sleep(1)
#Password
    password=driver.find_element(By.NAME,"Password")
    password.send_keys("")
    time.sleep(1)
#Log in
    log_in=driver.find_element(By.XPATH,"//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
    if driver.title == "Dashboard / nopCommerce administration":
        print("Welcome John Smith:",driver.title)

#catlog
        catalog=driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/nav/ul/li[2]/a/p")
        catalog.click()
        time.sleep(2)
        product=driver.find_element(By.XPATH,"/html/body/div[3]/aside/div/nav/ul/li[2]/ul/li[1]/a/p")
        product.click()
        time.sleep(2)
    else:
        print("you are not logged in correctly:",driver.title)
else:
    print("you are landed on wrong page and it's title is:", driver.title)
driver.quit()