print("\nExample 1 : Basic Function")

a = 10
b = 20
sum = a + b
print("Example 1 : ",sum)

# def -- > define a function
def add(a, b): # add is the function name, (a,b) are the parameters. (function's parameters)
    sum = a + b
    print(f"The sum of {a} and {b} is {sum}")
add(10,20)
add(5,2)

def subtract(x, y):
    subtract= x - y
    print(f"The sub of {x} and {y} is {subtract}")
subtract(x=10 ,y=5)

subtract(x=50,y=30)

print("\nExample 3 : Basic Function with return statement")
def add(a,b):
    sum = a + b
    return sum
result = add(10,20)
print(result)

def multiplication(w,z):
    multiplication=w*z
    return multiplication
result=multiplication(w=20, z=30)
print(result)
result=multiplication(w=200, z=80)
print(result)

def add(e,f):
    sum=e+f
    return sum
result=add(e=50,f=90)
print(result)

def subtract(u,i):
    subtract=u-i
    return subtract
result=subtract(u=70,i=40)
print(result)

print("\nExample 5 : Basic Function with default parameters")
def greet(name = "User"):
    return f"Hello, {name}" # this will return the value of welcome_message


print(greet("Credence"))
print(greet())
print("\nExample 6 : Basic Function with keyword parameters/keyword argument")


def add(a, b):
    sum = a + b
    print(f"The sum of {a} and {b} is {sum}")


add(10, 20)  # default use for calling function
add(a=10, b=20)  # you can write this way also, just to make it more readable, a and b --> keyword paraders
add(b=10, a=20)

# Example 7 : Basic Function with variable length parameters
print("\nExample 7 : Basic Function with variable length parameters")


def add(*args):  # *args --> variable length parameters # when you are not sure/aware about the number of parameters
    sum = 0  # sum --> local variable
    for i in args:  # for first iteration i = 10, for second iteration i = 20,
        sum = sum + i  # sum = sum + 10, sum = sum + 20,
    return sum


print(add(10, 20, 30, 40))
print(add(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))

# Example 8 : Nested Function for calculator
print("\nExample 8 : Nested Function for calculator")
'''
def add(a,b):
    sum = a + b
    return sum

def sub(a,b):
    sub = a - b
    return sub

print(f"The sum of 10 and 20 is {add(10,20)}") #    add(10,20)
print(f"The sum of 10 and 20 is {sub(10,20)}") #    add(10,20)
'''


def Calculator(a, b):  # Outer function
    def add():  # Inner function
        return print(f"The sum of {a} and {b} is {a + b}")

    def sub():  # Inner function
        return print(f"The sub of {a} and {b} is {a - b}")

    return add(), sub()  # here outer function is calling inner functions add and sub


Calculator(10, 20)
Calculator(30, 40)

# Example 9 : Global variable
print("\nExample 9 : Global variable")

score = 50  # global variable which is defined outside the function


# Global Variable :
# Variable which is define outside the function is called global variable.
# It use to store the values/data in memory.
# Global variable can be access inside and outside the function.
# Global variable can be modify inside and outside the function.
# Global variable can be access by any function/ multiple function.

def increase_score():
    global score  # this will make score as global variable
    score = score + 10
    return score


def decrease_score():
    global score  # this will make score as global variable
    score = score - 10
    return score


print(increase_score())
print(decrease_score())

# non-local variable
# Example 10 : non-local variable
print("\nExample 10 : non-local variable")


# Non local variable :
# Variable which is define inside the function is called local variable.
# It use to store the values/data in memory.
# Local variable can be access inside the function.
# Local variable can be modify inside the function.


def outer_function():
    x = 10  # local variable

    def inner_function():
        nonlocal x  # this will make x as non-local variable # byt using non local we can change the value of x which is defined inside the inner function
        x = x + 100
        return x

    return inner_function()


print(outer_function())


def out_fun():
    var = "this is local variable"

    def inner_fun():
        nonlocal var
        var = "this is non-local variable, updated by inner function"
        return var

    return inner_fun()


print(out_fun())

# Example 11 : Recursive Function
print("\nExample 11 : Recursive Function")

# Recursive Function :
# Function which call itself is called recursive function.
'''
What is factorial?
The factorial of a number is the product of all positive integers less than or equal to that number.

5 ! = 5 * 4 * 3 * 2 * 1 = 120
4 ! = 4 * 3 * 2 * 1 = 24
3 ! = 3 * 2 * 1 = 6
2 ! = 2 * 1 = 2
1 ! = 1 = 1
'''


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 5
'''
def factorial(5):
    if 5 == 1:
        return 1
    else:
        return 5 * factorial(5-1)

5*factorial(4)


def factorial(4):
    if 4 == 1:
        return 1
    else:
        return 4 * factorial(4-1)

5*4*factorial(3)


def factorial(3):
    if 3 == 1:
        return 1
    else:
        return 3 * factorial(3-1)

5*4*3*factorial(2)

def factorial(2):
    if 2 == 1:
        return 1
    else:
        return 2 * factorial(2-1)


5*4*3*2*factorial(1)

def factorial(1):
    if 1 == 1: # True
        return 1
    else: # this block will be not executed
        return 1 * factorial(1-1)


5*4*3*2*1


'''
# 100 ! = 100*99*98*97........*1
print(factorial(100))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))

# Write the program to find the factorial of a number using for loop.


# **Keyword Arguments (kwargs)

