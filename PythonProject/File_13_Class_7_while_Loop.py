## Example 1: Basic While Loop : print 1 to 5
print("\nExample 1 : Basic While Loop : print 1 to 5")
num=1
while num<=5:
    print("Example 1 : ", num)
    num=num+1

# Example 2 While loop with List
print("\nExample 2 : While loop with List")
list1 = [1, 2, 3, 4, 5]
num = 0
while num < len(list1):
    print("Example 2 : ", list1[num])
    num = num + 1

print("\n practice example 1")
list=[1,5,10,7,8]
num=0
while num< len(list):
    print(list[num])
    num=num+1



# Example : While loop
print("\nExample 3 : While loop")
while True:
    num = int(input("Enter a number : "))
    if num % 2 == 0:
        print("Example 3 : ", num, " : number is even")
        break
    else:
        print("Example 3 : ", num, " : number is odd. Please try again")
        num = num + 1
