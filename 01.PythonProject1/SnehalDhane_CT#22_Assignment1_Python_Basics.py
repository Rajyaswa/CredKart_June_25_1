#1. Basic Print Statement
#Write a Python program to print "Hello, Python!" to the console.

print("Hello, Python!")

#2. Single-Line Comment
# Use a single-line comment to explain the purpose of a print statement that displays "Hello, User!".

print("Hello, User!") # print statement displays the output

#3. Multi-Line Comment
#Use a multi-line comment to describe a program that adds two numbers and displays the result.
a=10
b=35
a+b
print(a+b)
""" 
Here  a and b are variable and store value 10 & 35 respectively,
to add this two numbers we write the (a+b),
to display the addition result we write syntax print(a+b)
         """
#4. Basic Addition
# Write a Python program that assigns values to num1 and num2, then prints their sum.
num1=30
num2=45
sum=num1+num2
print(sum)

#5. User Input Addition
# Modify the program from Question 4 to accept num1 and num2 as input from the user and then print their sum.




#6. Concatenate Strings Using Plus Operator
# Concatenate two strings using the + operator. Display the sentence: "Python programming is fun!".
text1="Python"
text2=" programming"
text3=" is"
text4=" fun!"
Sentence=text1+text2+text3+text4
print("Sentence=",Sentence)

#7. Concatenate Strings Using Comma
#Rewrite the concatenation from Question 6 using commas in the print statement instead of the + operator.
print(text1,text2,text3,text4)

#8. Multiple Line Print Using \n
# Use the newline character (\n) to print:
# Line 1
# Line 2
# Line 3
print("Line 1\nLine 2\nLine 3")

#9. Print Triple-Quoted String
# 9.Write a program that uses triple quotes to print:
# This is
# a multi-line
# print statement
print(""" \"This is\n a multi-line \n print statement\"""")
print(""" This is a multi-line print statement""")
print("This is\n a multi-line\n print statement")

#10. Escape Characters
# Write a Python program that displays this text with quotes: "Learning Python is fun!"
print("\"Learning Python is fun!\"")

#11. String with Variable
# Define a variable fruit = "apple" and print "I love eating apple" using the variable.
fruit = "apple"# variable
string= "I Love eating apple"# string
print("I love eating", fruit)

#12. Concatenation Using F-String
# Using an f-string,
# write a program that prints "My favorite fruit is apple" by assigning "apple" to a variable.
print(f"My favorite fruit is ","apple")

#13. Simple Variable Reassignment
# Write a program that defines a variable x with the value 10, then reassigns it to 20, and finally prints the new value of x
x=10
print("x=10")
x=20
print(f" x=10 :{x}")

#14. Display Name and City
# Create variables name and city with your name and city, respectively.
# Print "My name is [name] and I am from [city]" using these variables
Name= "Snehal"
City= "Kolhapur"
print("My name is",Name,",", "I am from",City)

#15. Use of \t for Tabs
# Use the tab escape character (\t)
# to print:
#Item    Price
#Apple   $1.50
#Banana  $0.75
print("Item\tPrice")
print("Apple\t$1.50")
print("Item\t$0.75")

#16. Multi-line Comment for Code Explanation
# 16.Use a multi-line comment to explain the code logic of a program
# that calculates the area of a rectangle with length = 5 and width = 3
length = 5
width = 3
Area=length*width
print(f"Rectangle Area=",Area)
''''here we store the value of length by (length=5) also store the value of width by (width=3)
then for calculates the rectangle write the syntax (Area=length*width)
to display the area =print(f"Rectangle Area=",Area) '''

#17. Modify Print Using Escape Character
#17.Write a program that prints "I am learning \"Python\" programming!" using escape characters.
print("\"I am learning \"Python\" programming!\"" )

#18. Assign and Print
# 18.Define two variables, language = "Python" and tool = "PyCharm". Print "I use Python in PyCharm" by combining these variables
language = "Python"
tool = "PyCharm"
print("I use",language,"in",tool)

#19. Arithmetic Operations
# 19.Write a Python program to perform addition, subtraction, multiplication, and division of two numbers (a = 15, b = 3)
# and print the results
a = 15
b = 3
print("Addition=",a+b)
print(a+b)
print("Subtraction=",a-b)
print(a-b)
print("Multiplication=",a*b)
print(a*b)
print("division=",a/b)
print(a/b)
print("division=",a//b)
print(a//b)

#20. Display Variable in Sentence Using F-String
# 20.Use an f-string to display "The result of adding 10 and 20 is 30" where 10, 20, and 30 are values stored in variables.
x=10
y=20
z=30
print(f"The result of adding 10 and 20 is 30=",x+y+z)
