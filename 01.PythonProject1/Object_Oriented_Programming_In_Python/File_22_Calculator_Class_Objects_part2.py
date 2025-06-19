class Calculator: #syntax : class class_name
    power_source = "Battery"

    def add(self, a, b):  # function # function which is defined in class is called method / instance method
        sum = a + b
        print(f"The sum of {a} and {b} is {sum}")

    def sub(self, a, b):
        sub = a - b
        print(f"The sub of {a} and {b} is {sub}")

    def mul(self, a, b):
        mul = a * b
        print(f"The mul of {a} and {b} is {mul}")

    def cal_info(self):  # syntax : def function_name(self, parameters):
        print(f"The power source of this calculator is {self.power_source}")
cal1 = Calculator()
cal2 = Calculator()
print(f"cal1.power_source: {cal1.power_source}") # Checking the value of power source is nothing but the accessing the class attribute.
print(f"cal2.power_source: {cal2.power_source}")


cal1.power_source = "solar panel"
cal2.power_source = "Rechargeable Battery"
print(f"cal1.power_source: {cal1.power_source}")  # Battery
print(f"cal2.power_source: {cal2.power_source}")

# 04. Directly accessing the class attribute thr class name.
print("\n04. Directly accessing the class attribute thr class name.")
#syntax : class_name.class_attribute
print(f"Calculator.power_source: {Calculator.power_source}")
Calculator.power_source = "Mains" # you are change the data in class template directly


cal3 = Calculator()
print(f"cal3.power_source: {cal3.power_source}")


# 05. Access the instance method (add, sub, mul)
print("\n05. Access the instance method (add, sub, mul)")
# syntax : object_name.function_name()
cal1.add(10,20)
cal1.sub(10,20)
cal1.mul(10,20)
cal1.cal_info()
cal2.cal_info()