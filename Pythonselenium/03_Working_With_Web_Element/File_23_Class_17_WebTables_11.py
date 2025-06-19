
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()


# Web table

table_rows = driver.find_elements(By.XPATH, "//table[@id='product']/tbody/tr")
# //table[@id='product']/tbody/tr --> Relative XPATH
# /html[1]/body[1]/div[1]/div[1]/fieldset[3] --> Absolute XPATH

print("Number of rows in the table:", len(table_rows))


for row in range(1, len(table_rows)+1): # 1,11
    Instructor = driver.find_element(By.XPATH, f"//table[@id='product']/tbody/tr[{row}]/td[1]").text
    Course = driver.find_element(By.XPATH, f"//table[@id='product']/tbody/tr[{row}]/td[2]").text
    Price = driver.find_element(By.XPATH, f"//table[@id='product']/tbody/tr[{row}]/td[3]").text
    # print(Instructor)
    # print(Course)
    # print(Price)
    print(f"Row no {row}--> Instructor : {Instructor}, Course : {Course}, Price : {Price}")



# Write this data in excel file--> you task




