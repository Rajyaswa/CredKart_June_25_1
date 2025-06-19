print("Example 1 : Basic If Statement")
a = 10
b = 20
if a > b:  # False
    print("1 : a is greater than b")  # that's why this statement is not executed.

if a < b:  # True
    print("2: a is less than b")  # that's why this statement is executed.

# Example 2 : If-else Statement
print("\nExample 2 : If-Else Statement")

num = 4

if num > 0:  # here number is positive # True
    print("Number is positive")  # that's why this statement is executed
else:
    print("Number is negative")

num = -2

if num > 0:  # here number is negative # False
    print("Number is positive")
else:  # that's why this statement is executed # if statement is false
    print("Number is negative")  # This statement is executed

# Example 3 : If-elif-else Statement
print("\nExample 3 : If-Elif-Else Statement")

num = 1
if num > 0:  # True
    print("Number is positive")  # that's why this statement is executed
elif num == 0:  # this is not executed
    print("Number is zero")
else:  # this is not executed
    print("Number is negative")

num = 0
if num > 0:  # False
    print("Number is positive")  # that's why this statement is not executed
elif num == 0:  # True
    print("Number is zero")  # that's why this statement is executed
else:  # this is not executed # this will execute if both if and elif statement is false
    print("Number is negative")

num = -5
if num > 0:  # False
    print("Number is positive")  # this is not executed
elif num == 0:  # False
    print("Number is zero")  # this is not executed
else:  # this is executed
    print("Number is negative")  # this is executed

# if --> one
# elif --> multiple
# else --> one


karma = "Good"
if karma == "Good":
    print("You are a good person, you will be in heaven")
else:
    print("Karma karo, kand mat karo")
