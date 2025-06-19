class Calculator:
    power_source="Battery"

# 01. Create an object of the class Calculator / Instance of the class
print("01. Create an object of the class Calculator / Instance of the class")
# Syntax : object_name = class_name()
cal1 = Calculator()
cal2 = Calculator()

# 02. Access the class attribute (power_source).
print("\n02. Access the class attribute (power_source)")
# syntax : object_name.class_attribute
print(f"cal1.power_source: {cal1.power_source}") # Checking the value of power source is nothing but the accessing the class attribute.
print(f"cal2.power_source: {cal2.power_source}")

# 03. Change the class attribute (power_source).
print("\n03. Change the class attribute (power_source)")
# syntax : object_name.class_attribute = new_value
cal1.power_source = "solar panel"
cal2.power_source = "Rechargeable Battery"
print(f"cal1.power_source: {cal1.power_source}")  # Battery
print(f"cal2.power_source: {cal2.power_source}") # Rechargeable Battery


# 04. Directly accessing the class attribute thr class name.
print("\n04. Directly accessing the class attribute thr class name.")
#syntax : class_name.class_attribute
print(f"Calculator.power_source: {Calculator.power_source}")
Calculator.power_source = "Mains" # you are change the data in class template directly


cal3 = Calculator()
print(f"cal3.power_source: {cal3.power_source}")