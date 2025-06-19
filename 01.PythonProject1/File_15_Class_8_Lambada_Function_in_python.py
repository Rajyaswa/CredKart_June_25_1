# Example 1 : Basic Lambda Function
print("\nExample 1 : Basic Lambda Function")
def add(a,b):
    return a+b
print(add(10,20)) # 30

add= lambda a,b :a+b
print(add(10,20)) # 30

# Example 2 : Basic Lambda Function
print("\nExample 2 : Basic Lambda Function")

subtract=lambda x,y :x-y
print(subtract(x=56,y=30))

mul=lambda p,q: p*q
print(mul(p=15,q=30))

square = lambda x : x**2
print(square(5))

# Example 3 : Basic Lambda Function
print("\nExample 3 : Basic Lambda Function")
cube=lambda x:x**3
print(cube(6))

# Exmaple 4 : Basic Lambda Function
print("\nExample 4 : Basic Lambda Function")
def compare (num1 ,num2):
    if num1 > num2 :
        return num1
    else:
        return num2
print(f"Compare : {compare(10, 11)}")  # compare(10,11)

compare=lambda num1 , num2 : num1 if num1 > num2 else num2
print(f"Compare : {compare(10,11)}")


# Example 5 : Basic Lambda Function

def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(f"Check even : {check_even(5)}") # False

check_even = lambda num : True if num % 2 == 0 else False

print(f"Check even : {check_even(5)}")