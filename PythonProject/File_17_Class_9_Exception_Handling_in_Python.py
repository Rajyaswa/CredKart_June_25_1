# Example 1 : Basic exception handling
print("\nExample 1 : Basic exception handling")
try :
    a = 5/0 # this will raise an exception : ZeroDivisionError
except:
    print("Example1  : You can't divide by zero")


try:
    a= 5/6
except:
    print("you can not divide")

# Example 2 : Basic exception handling
print("\nExample 2 : Basic exception handling")
try :
    b =  "Hello" + 5 # this will raise an exception : TypeError
except:
    print("Example2  : You can't add string and integer")

#Example 3 : Basic exception handling
print("\nExample 3 : Basic exception handling")
try :
    b =  "Hello" + 7
    print("Example 3: you can add string and integer, covert int to string")
except :
    print("An error occurred in Example 3")


# Example 4 : Basic exception handling
print("\nExample 4 : Basic exception handling")

list1 = [1, 2, 3, 4, 5]

#print(list1[10])

try :
    print(f"Example 4: {list1[1]}") # this will raise an exception : IndexError (list1[3])
except IndexError as err:
    print("Example 4: IndexError : ", err)

print("\nExample 2: ValueError handling")

try:
    num = int("abc")  # This will cause a ValueError
except ValueError:
    print("Caught a ValueError: Cannot convert letters to an integer.")


# Example 5 : Exception handling with else block and finally block
print("\nExample 5 : Exception handling with else block and finally block")

try :
    num = int(input("Enter a number : "))  # if no error then try block will be executed
    print(f"Example 5: {num}")
except ValueError as err: # if error then except block will be executed
    print("Example 5: ValueError : ", err, "Please enter a valid number")
else: # Optional block
    print("Example 5: No error") # execute when try block will not raise any error
finally: # Always execute # Optional block
    print("Example 5: Finally block")

