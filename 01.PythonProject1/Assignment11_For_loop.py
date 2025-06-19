#==============Simple Questions (1–15)============================
# 1.Write a loop to print numbers from 1 to 10 using a for loop.
print("\nQuestion1:Write a loop to print numbers from 1 to 10 using a for loop.")
range(1,10)
print(range(1,10))
for i  in range(1,10):
    print(f"Range={i}")

# 2.Iterate through a list of colors (red, blue, green) and print each color.
print("\nQuestion2:Iterate through a list of colors (red, blue, green) and print each color.")
list=["red","blue","greeen"]
print(list)
for i in list:
    print(f"item of list = {i}")

# 3.Loop through the characters of the string "Python" and print them.
print("\nQuestion3:Loop through the characters of the string \"Python\" and print them.")
string="Python"
print(f"string={string}")
for i in string:
    print(f"character of string = {i}")

# 4.Use a for loop to print the square of numbers from 1 to 5.
print("\nQuestion4.Use a for loop to print the square of numbers from 1 to 5.")
range(1,5)
print(range(1,5))
for i in range(1,5):
    print(f"square of {i} = {i**2} ")

# 5.Write a loop to count and print the number of vowels in the string "education".
print("\nQuestion5:Write a loop to count and print the number of vowels in the string\"education\".")
string="education"
print(f"string={string}")
for i in string:
    if "a" or "e" or "i" or "o" or "u " in string:
     print(f"count of string,{string.count(i)}")


# 6.Iterate through a list of numbers [2, 4, 6, 8, 10] and print only the even numbers.
print("\nQuestion:6.Iterate through a list of numbers [2, 4, 6, 8, 10] and print only the even numbers.")
list=[2,4,6,8,10]
print(f"list ={list}")
for i in list:
     if i % 2==0:
         print("even num",i)

# 7.Use range() to print numbers from 10 to 1 in reverse order.
print("\nQuestion7:Use range() to print numbers from 10 to 1 in reverse order.")
range(11,0)
for i in range (11,0):
    print(i)

# 8.Print the multiplication table for 3 using a loop.
print("\nQuestion8.Print the multiplication table for 3 using a loop.")
range(1,11)
for i in range(1,11):
    print(f"table of 3 is :",i,"*","3","=",i*3)

# 9.Loop through a list of integers and calculate the sum of all elements.
list=[1,2,4,5]
for i in list:
    #sum += i:
    print(sum)
# 10.Write a loop to count how many times the letter "a" appears in the string "banana".
string="banana"
print(string.count("a"))
# 11.Create a for loop to iterate through a tuple containing the names of three fruits and print each one.
# 12.Write a loop to find the maximum value in a list of integers.
# 13.Iterate over a dictionary with keys name, age, and city, and print each key-value pair.
# 14.Use a for loop to check if a number is present in a list.
