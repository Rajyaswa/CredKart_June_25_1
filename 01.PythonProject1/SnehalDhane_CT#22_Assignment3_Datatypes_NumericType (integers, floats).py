##============================1.Integers ======================================================
# 1.Define an integer variable x with a value of 20. Print its type using the type() function.
x=20
print(type(x))
print(f"Type of x is ={type(x)}")

# 2.Using a = 10 and b = 5, perform and print the result of integer division using the // operator.
a = 10
b = 5
print(f"result of integer division ={a//b}")

# 3.Define an integer variable n = -15. Use the abs() function to find and print its absolute value.
n=-15
print(f"absolute value of n is ={abs(n)}")

# 4.Calculate 7 ** 3 using integers and print the result.
x=7
y=3
print(f"result of 7 ** 3 is ={7 ** 3} ")

# 5.Using num = 37, calculate the result of num % 10 and explain what the modulus represents.
num = 37
result = num % 10
print(f"Result of num % 10:{result}") #The modulus operator (%)  gives the remainder

# 6.Define two integer variables, x = 100 and y = 50. Find and print the maximum value using the max() function.
x = 100
y = 50
print(f"maximum value in x and y ;= {max(x,y)}")

# 7.Define a = 12 and b = 8. Calculate the result of a + b * 3 and explain operator precedence in your answer.
a = 12
b = 8
print(f"the result of a + b * 3 is = { a + b * 3}")
""" In this code the system excute the arithmatic operation b*3 (multipilcation)
after that system shift to next arithmatic that is a + result of b*3 """

# 8.Use the sum() function to find the sum of the integers in the list [3, 5, -7, 10].
list =[3, 5, -7, 10]
print(f"sum of the integers is ={sum(list)}")

# 9.Convert the string "45" to an integer and multiply it by 2.
string="45"
print(f" result of multiply by 2 is ={int(string)*2}")

# 10.Define n = 1024. Calculate and print the square root of n using exponentiation (**).
n=2024
print(f"the square root of n is ={n**0.5}")

#11.Using a = -10 and b = 3, calculate and print a // b.
a = -10
b = 3
print(f" result of a // b is = {a // b}")

# 12.Define n = 25. Convert it to a float and print the result.
n=25
print(f"conversion of n in float is ={float(n)}")

# 13.Using divmod(), find both the quotient and remainder of 53 divided by 7.
a=53
b=7
print(f"both the quotient and remainder is ={divmod(a,b)}")

# 14.Define x = 10. Use the pow() function to calculate x raised to the power of 4.
x=10
print(f"result of x power 4 is ={pow(x,4) }")

# 15.Calculate 15 -4 * 3 + 2 and explain the order of operations.
print(f" The result of (15 -4 * 3 + 2) is = {15 -4 * 3 + 2}")
"""" order of above code is according to BODMAS means firstly arithamatic operation -4*3=-12 is performed 
after that it move forwation 1ard to next operation result of (-4*3)+2 that is -12 + 2=-10,  
then it comes to last oper 15-10 
and finnally print the result should be 5"""

# 16.Define a = 8, b = -3, and c = 12. Find and print the minimum value using the min() function.
a = 8
b = -3
c = 12
print(f"The Minimum value between a,b,c is = {min(a,b,c)}")

# 17.Using a = 14, print the result of a % 3.
a=14
print(f"the result of a % 3 ={a%3}")

# 18.Define an integer x = 3. Double it using multiplication and print the result.
x = 3
print(f"Double of x is ={x*2}")

# 19.Define num1 = 18 and num2 = 4. Calculate num1 % num2 and explain the modulus operation result.
num1 = 18
num2 = 4
Result=num1 % num2
print(f"result of num1 % num2 is ={num1 % num2}")#The modulus operator (%)  gives the remainder

# 20.Define an integer variable, convert it to a string, and concatenate it with " is an integer".
x=25
print(f"conversion of integer to string,concatenate it with  is an integer ={str(int(x))+(" is an integer")}")

#========================2.Floats=======================================================
# 1.Define a float variable a = 5.5. Print its type using the type() function.
a = 5.5
print(f"type of a is ={type(a)}")

# 2.Using x = 4.2 and y = 2.1, calculate x + y and print the result.
x = 4.2
y = 2.1
print(f" The result of x + y is = {x + y}")

# 3.Using price = 99.99, round it to the nearest integer using the round() function.
price = 99.99
print(f"round of price to the nearest integer is = {round(price)}")

# 4.Define a = 7.5 and b = 2.5. Calculate a -b and print the result.
a = 7.5
b = 2.5
print(f"The result of a-b is ={a-b}")

# 5.Convert the string "45.67" to a float and divide it by 2.
string= "45.67"
print(f" The result conversion of string in float and dividation of it by 2 is = {float(string)/2}")

#6.Define a float x = 3.7. Convert it to an integer and explain what happens to the decimal portion.
x = 3.7
print(f"the conversion of float to integer is ={int(float(x))}")
#int(x) converts the float to an integer by deleting the decimal part (it does not round).
#So int(3.7) becomes 3.

# 7.Using x = 5.3 and y = 2.6, calculate x * y and print the result.
x = 5.3
y = 2.6
print(f"the result of x*y is ={x*y}")

# 8.Define temp = -2.4. Use the abs() function to print the absolute value.
temp = -2.4
print(f"the absolute value of temp is ={abs(temp)}")

# 9.Using a = 12.0 and b = 4.0, calculate and print the result of a / b.
a = 12.0
b = 4.0
print(f"the result of a / b is = {a / b}")

# 10.Define x = 2.5. Use pow() to calculate and print x raised to the power of 3.
x = 2.5
print(f" the result of x raised to the power of 3 is = {pow(x,3)}")

# 11.Using price = 99.99, round it to one decimal place.
price = 99.99
print(f"round of price to one decimal place is ={round(price,1)}")

# 12.Define y = -15.6. Find and print the ceiling value using math.ceil() (requires import math).
import math

y = -15.6
ceiling_value = math.ceil(y)
print(f"The ceiling value of {y} is {ceiling_value}")


# 13.Using x = 7.8, calculate x // 2 and explain what the result represents.
x = 7.8
print(f"the result  of x // 2 is ={x // 2}") #The // operator is floor division.
# It divides and rounds down  to the nearest whole number

# 14.Define base = 4.5 and exp = 2.0. Calculate and print base ** exp.
base = 4.5
exp = 2.0
print(f"The result of base ** exp is ={base ** exp}")

# 15.Define a float pi = 3.14159. Use round() to round pi to two decimal places.
pi = 3.14159
print(f"Round of pi upto 2 decimal is ={round(pi,2)}")

# 16.Using x = 6.7 and y = 2.3, calculate and print x % y.
x = 6.7
y = 2.3
print(f"the result of x % y is ={x % y} ")

# 17.Using x = 12.9, convert it to an integer and print the result.
x = 12.9
print(f"conversion of float x into integer is ={int(float(x))}")

# 18.Using x = 5.6, find and print the result of x ** 2.
x = 5.6
print(f"the result of x ** 2 is ={x ** 2}")

# 19.Convert the float 100.75 to an integer and explain what happens to the decimal portion.
x=100.75
print(f"conversion of float x into integer is ={int(float(x))}")
#int(100.75) removes the decimal portion.
# It does not round — it simply truncates everything after the decimal point.

# 20.Define a float number = 10.45, convert it to a string, and concatenate it with " is a float".
number = 10.45
print(f"conversion of integer to string,concatenate it with  is an integer ={str(float(number))+(" is a float")}")

