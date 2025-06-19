# What is Loop in python ?
# Loops in python are use to repart block of code multiple times,
#  which helps us to reduce repetition and efficient and more readable code.
# There are two types of loop
# 1. For Loop
# 2. While Loop

# For Loop
# used to iterate over a sequence (Like Range,list, tuple, dict, set, or string)
# Use for loop when you know the number of iteration.
# For loop is used to iterate over a sequence of items.
# Loop is mostly use for repeating the same task.

# Example 1 :Basic For loop
print("\nExample 1 :Basic For loop")
for i in range(1,6): # i --> iterator/ Loop variable # range(1,6) -- > sequence, how many times loop will run
    print("Example 1 : ",i)

#Example 2: Basic For loop
print("\nExample 2: Basic For loop")
list1 = [1, 2, 3, 4, 5]
for i in list1:
    print("Example 2: ",i)

# Example 3: Basic for loop
print("\nexample 3: Basic For loop")
list2=[1,2,3,4,5]
for i in list2:
    print("Example 3:",i**2)

# Example 4: Basic for loop
print("\n Example :4 Basic For Loop")
list=[3,4,5,6]
for i in list:
    print("Example 4:",i**3)

# Example 5: Basic for loop
print("\nExample :5 Basic For Loop")
range6=[1,11]
for i in range6 :
    print("example 5:",i*2)

# Example 6: Basic For Loop
print("\nExample 4 :Basic For loop :  print the squares of numbers from 1 to 10")
for num in range(1,11):
    print("Example 4 : ","Loop no.",num  ,"Square of ", num, "is ",num**2)

print("\nExample A : Basic For Loop : print the table of 2")
for num in range (1,11):
    print("Example A :", "Loop no.",num,"multiplied by",num,"is" ,num*2)

print("\ntable 3")
for num in range(1,11):
    print("table3 :","loop no.",num,"has to 3",num,"is",num*3)

print("\n table4")
for num in range(1,11):
    print(" table 4 | 4*1=",num*4)

print("\ntable of 5")
for num in range(1,11):
    print("table of 5| 5*1=",num*5)

print("\ntable of 6")
for num in range (1,11):
    print("table of 6| 6*",num,"=",num*6)

print("\n practice of for loop")
list6=[1,2,3,4,5]
for i in list6:
    print(" practice of for loop",i*9)

# Example of string iteration
string="i love my India"
for i in string:
    print("string",i)

# Example 6 : Basic For loop with if statement
list=[1,2,3,4,5,6,7,8,9]
for item in list:
    if item % 2 ==0:
     print(item,"item is even",)
    else:
        print(item,"item is odd")\

# Example 7 : For Loop with break statement
print("\nExample 7 : For Loop with break statement")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in list1:
    if item == 5: # condition true
        break # it will break the loop mean it will stop the loop or exit from loop
    print("Example 7 : ", item)

# Example 8 : For Loop with continue statement
print("\nExample 8 : For Loop with continue statement")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in list1:
    if item == 5: # for item '5' loop will skip the iteration and continue for next
        continue
    print("Example 8 : ",item)

# Example 9 : For Loop with pass statement
print("\nExample 9 : For Loop with pass statement")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in list1:
    pass # pass statement does not do anything # it is used to avoid error # we are writing pass just to indicate that we will wire the code in future


# Example 10 : For Loop with tuple
print("\nExample 10 : For Loop with tuple")
colors = ("red", "green", "blue")
for color in colors:
    print("Example 10 : ",color)

# Example 11 : For Loop with dictionary
print("\nExample 11 : For Loop with dictionary")
colors = {"a": 1, "b": 2, "c": 3}
for key in colors:
    print("Example 11 : ", key, ":", colors[key])

# Example 12 : For Loop with set
print("\nExample 12 : For Loop with set")
colors = {"red", "green", "blue"}
for color in colors:
    print("Example 12 : ",color)

# Example 13 : Nested For Loop
print("\nExample 13 : Nested For Loop")
for i in range(1,4): # outer loop # this will run 3 times # i = 1,2,3
    for j in range(1,4): # inner loop # this will run 3 times # j = 1,2,3
        print("Example 13 : ",i,j)

# Example 14 : Nested For Loop
print("\nExample 14 : Nested For Loop")
text = "abc"
for i in text: # outer loop  # i = C, r, e, d, e, n, c, e 8 times
    for j in range(1,4): # inner loop # 2 times
        print("Example 14 : ",i,j)

print("\nExample 15 : Nested For Loop with break")
text = "abc"
for i in text: # outer loop  # i = C, r, e, d, e, n, c, e 8 times
    for j in range(1,6): # inner loop # 5 times
        if j == 3: # condition true
            break
        print("Example 15 : ",i,j)

# Example 16 : Nested For Loop
print("\nExample 16 : Nested For Loop with continue")
text = "abc"
for i in text:  # outer loop  # i = C, r, e, d, e, n, c, e 8 times
    for j in range(1, 6):  # inner loop # 5 times
        if j == 3:  # condition true
            continue
        print("Example 16 : ", i, j)

# Example 17 : Nested For Loop
print("\nExmaple 17 : Nested For Loop with pass")
text = "abc"
for i in text:  # outer loop  # i = C, r, e, d, e, n, c, e 8 times
    for j in range(1, 6):  # inner loop # 5 times
        pass

# Example 18 : For loop with else
print("\nExample 18 : For loop with else")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in list1:
    print("Example 18 : ",item)
else:
    print("Example 18 : Loop is completed")



# Example 19 : Enumerate function # enumerate -- > (index, value)
print("\nExample 19 : Enumerate function")
list1 =["red", "green", "blue", "yellow", "orange"]
for index, color in enumerate(list1):
    print("Example 19 : ",index, "index,", color, "color")