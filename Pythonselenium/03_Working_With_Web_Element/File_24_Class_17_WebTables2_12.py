from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
wb = Workbook()
ws = wb.active


driver = webdriver.Chrome()
driver.get("https://www.worldometers.info/world-population/population-by-country/")
driver.maximize_window()


# Web table Population

table_rows = driver.find_elements(By.XPATH, "//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr")

print("Number of rows in the table:", len(table_rows))


for row in range(1, len(table_rows)+1): # 1,11
    Sr_no = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[1]").text
    Countries = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[2]").text
    Population = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[3]").text
    Yearly_Change = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[4]").text
    Net_Change = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[5]").text
    Density = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[6]").text
    Land_Area = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[7]").text
    Migrants = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[8]").text
    Fert_Rate = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[9]").text
    Med_Age = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[10]").text
    Urban_Pop = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[11]").text
    World_Share = driver.find_element(By.XPATH, f"//table[@class='datatable w-full border border-zinc-200 datatable-table']/tbody/tr[{row}]/td[12]").text
    #print(Sr_no)

    print(f"Sr_no:{Sr_no}, Country : {Countries}, Population : {Population}, Yearly_Change : {Yearly_Change}, Net_Change : {Net_Change},Density : {Density}, Land_Area : {Land_Area}, Migrants : {Migrants}, Fert_Rate : {Fert_Rate}, Med_Age : {Med_Age}, Urban_Pop : {Urban_Pop},World_Share : {World_Share}")
    ws.append([Sr_no, Countries, Population, Yearly_Change, Net_Change, Density, Land_Area, Migrants, Fert_Rate, Med_Age, Urban_Pop, World_Share])


wb.save("Web_Table_Data2.xlsx")

# Write this data in excel file--> you task




