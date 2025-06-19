from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook

# Setup Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://apps.credence.in/practice")
driver.maximize_window()

# Get all table rows
table_rows = driver.find_elements(By.XPATH, "//table[@id='product']/tbody/tr")
print("Number of rows in the table:", len(table_rows))

# Create a new Excel workbook
wb = Workbook()
ws = wb.active
ws.title = "Web Table Data"

# Add headers
ws.append(["Instructor", "Course", "Price"])

# Loop through table and collect data
for row in range(1, len(table_rows) + 1):
    instructor = driver.find_element(By.XPATH, f"//table[@id='product']/tbody/tr[{row}]/td[1]").text
    course = driver.find_element(By.XPATH, f"//table[@id='product']/tbody/tr[{row}]/td[2]").text
    price = driver.find_element(By.XPATH, f"//table[@id='product']/tbody/tr[{row}]/td[3]").text
    print(f"Row {row} --> Instructor: {instructor}, Course: {course}, Price: {price}")

    # Write row to Excel
    ws.append([instructor, course, price])

# Save the Excel file
wb.save("Web_Table_Data1.xlsx")

# Close browser
driver.quit()

print("✅ Data written to Excel file 'Web_Table_Data.xlsx'")
