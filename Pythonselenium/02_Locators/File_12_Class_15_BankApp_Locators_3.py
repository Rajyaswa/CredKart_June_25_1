'''

List of all locators available in Python selenium :
1. id
2. name
3. class_name
4. tag_name
5. link_text
6. partial_link_text
7. css_selector
8. xpath

'''

'''
<input id="username" name="username" type="text" class="inputField" required="" minlength="6" maxlength="20" placeholder="Enter username (6-20 alphanumeric)">

# Tagname : input
# Attribute : id, name, type, class etc..
# Value : username,usernmae, text,inputField etc.. 

'''

#XPath Format : //tagname[@attribute='value'] --> one way to write


# XPATH--> XPATH(XML Path Language) is used language to select elements
# or attribute from web pages
# XPATH Format --> //tagname[@attribute='value']
# To check Xpath in browser console --> $x("Xpath")



# CSS_SELECTOR format --> tagname[attribute='value'] --> one way to write
# CSS--> CSS(Cascading style sheets) is language used to describe
# presentation of web pages.
# CSS define visual properties of element like front, front size, colour, layout
# CSS format --> tagname[attribute='value']
# password css --> input[id='password']
# To check CSS in browser console --> $$("CSS")





import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/user.html")
driver.maximize_window()
#time.sleep(2)
print("Title of the page:", driver.title)

# Enter Username
time.sleep(2)
username = driver.find_element(By.XPATH, "//input[@name='username']")
username.send_keys("Credence123")


# Enter Password
time.sleep(2)
password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password.send_keys("Credence@123")

# Enter email
time.sleep(2)
email=driver.find_element(By.CSS_SELECTOR,"input[type='email']")
email.send_keys("soanl18055@gmail.com")

# Enter password
time.sleep(5)
phone = driver.find_element(By.NAME, "phone")
phone.send_keys("7895453225")

create_user_button = driver.find_element(By.ID, "createUserButton")
create_user_button.click()

login_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Login")
login_link.click()

time.sleep(10)

driver.quit()

time.sleep(6)
# Python "D:\Batch Notes\Automation Testing may 2025\02. Python Selenium\02. 02_Locators\File_10_Class_14_BankApp_Locators_1.py"
