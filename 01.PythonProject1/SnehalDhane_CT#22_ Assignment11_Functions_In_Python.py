#============Basic Function Concepts=======================
# 1.Write a function named multiply that multiplies two numbers and returns the result.
print("\nQuestion1:Write a function named multiply that multiplies two numbers and returns the result.")
def multiplication(a, b):
    sum= a * b
    return sum
print(f"result of two number multiplication={multiplication(15,12)}")

# 2.Define a function called print_greeting that takes no arguments and prints "Good Morning!".
print("\nQuestion2.Define a function called print_greeting that takes no arguments and prints \"Good Morning!\"")
def greeting():
    return ("Good Morning!")
result=greeting()
print(result)
# 3.Create a function subtract that takes two numbers as arguments and returns their difference.
print("\nQuestion3:Create a function subtract that takes two numbers as arguments and returns their difference.")
def subtract(num1,num2):
    subtract=num1-num2
    return subtract
print(f"return of two number subtract={subtract(15,12)}")
# 4.Write a function divide that divides two numbers and handles the case where the second number is zero by returning "Cannot divide by zero".
print("\n4.Write a function divide that divides two numbers and handles the case where the second number is zero by returning \"Cannot divide by zero\".")
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        result = a / b
        return result

print(f" result of dividation two numbers={divide(15,0)}")
print(f" result of dividation two numbers={divide(15,5)}")

# 5.Define a function concat_strings that takes two string arguments and returns their concatenation.
print("\nQuestion5:Define a function concat_strings that takes two string arguments and returns their concatenation.")
string1="Hi.."
string2="How are You?"
def add(string1,string2):
    return(string1+string2)
result=add("\nhi..","\nHow are You?")
print(f"result of concatenation of two string by function is={result}")
#===============================Functions with Default Parameters================================================
# 6.Create a function welcome_user that takes a name as a parameter and defaults to "Guest" if no name is provided.
print("\nQuestion6:Create a function welcome_user that takes a name as a parameter and defaults to \"Guest\" if no name is provided.")
def welcome(name="guest"):
    print("welcome",name)
welcome("snehal")
welcome()
# 7.Write a function calculate_total that takes two arguments: price and
# tax_rate with a default value of 0.1, and calculates the total amount.
print("\nQuestion7:Write a function calculate_total that takes two arguments: price and tax_rate with a default value of 0.1, and calculates the total amount")
def calculate_total(price,tax_rate=0.1):
    return f"total amount={price+(price*tax_rate)}"
print(calculate_total(100,0.1))
print(calculate_total(200,0.1))
#8.Define a function power that calculates the power of a number, where the exponent defaults to 2.
print("\nQuestion8:Define a function power that calculates the power of a number, where the exponent defaults to 2.")
def power(num,power=2):
    return f"power of number{num**2}"
print(power(4))

# ================================Keyword Arguments=================================================
# 9.Write a function user_info that accepts keyword arguments name and age and prints them.
print("\nQuestion9:Write a function user_info that accepts keyword arguments name and age and prints them.")
def user_info(name,age):
     return f" user_info\t user_name={name},\t age={age}"
print(user_info("snehal",30))
print(user_info("swaroop",33))

# 10.Create a function car_info that accepts the keyword arguments brand, model, and year to describe a car.
print("\nQuestion10:Create a function car_info that accepts the keyword arguments brand, model, and year to describe a car.")
def car_info(brand,model,year):
    return f"car_info \t brand={brand},\t age={year}"
print(car_info("nisan","magnite",2015))
print(car_info("TaTa","tiago",2013))

# ======================*Variable Arguments (args)===========================================
# 11.Define a function sum_all that accepts any number of arguments and returns their sum.
print("\nQuestion11:Define a function sum_all that accepts any number of arguments and returns their sum.")
def add(a,b):
    sum = a + b
    print(f"The sum of {a} and {b} is {sum}")

add(10,20)

# 12.Write a function average that calculates the average of all numbers passed as arguments.
#print("\nQuestion12:Write a function average that calculates the average of all numbers passed as arguments.")
#def avg(*args): # *args --> variable length parameters # when you are not sure/aware about the number of parameters
    #sum = 0 # sum --> local variable
    #for i in args: # for first iteration i = 10, for second iteration i = 20,
       #sum = (sum + i) / count(i)# sum = sum + 10, sum = sum + 20,
    #return sum
#print(avg(10,20,3))
# 13.Create a function max_number that finds the largest number from the arguments provided.
print("\nQuestion:13 Create a function max_number that finds the largest number from the arguments provided.")
def max_number(*args):
    return max_number()
print(max_number(10,20,30,40,75))
# =========================**Keyword Arguments (kwargs)==============================================
# 14.Write a function display_settings that accepts keyword arguments and prints them in the format: key -> value.
