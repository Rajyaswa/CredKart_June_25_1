#=================Basic if Statements====================================
# 1.Write a program to check if a number is greater than 10.
print("\nQuestion 1:Program to check if a number is greater than 10")
a=30
if a>10:
    print(f"a is greater than 10")
if a<10:
    print(f"a i smaller than b")

# 2.Check if a string contains the word "Python."
print("\nQuestion 2:Check if a string contains the word Python")
string="For paython credence is best solution"
print(f"String=\"{string}\"")
if "paython" in string:
    print("\"paython\" contain in string")
if "paython"  not in string:
    print("\"paython\" contain not in string")

# 3.Verify if a number is positive and print "Positive Number" if True.
print("\nQuestion 3:if a number is positive and print Positive Number if True")
num=10
if num >-1:
    print(f"\"Positive Number\"")
if num <-1:
    print(f"\"Negative Number\"")

# 4.Write a condition to check if a character in a string is uppercase.
#print(" condition to check if a character in a string is uppercase")
#string=""
# 5.Check if a variable contains the value None.
# ==========================if-else Statements=================================
# 6.Write a program to check if a number is odd or even.
print("\nquestion 6:Write a program to check if a number is odd or even")
num=15
if num % 2 == 0:
    print(f"The number {num} is Even.")
else:
    print(f"The number {num} is Odd.")
# 7.Check if a string starts with the letter "A" and print appropriate messages.
print("\nQuestion 7: Check if a string starts with the letter \"A\" and print appropriate messages.")
String="Amazon"
print(f"String=\"{String}\"")
if String.startswith("A"):
    print("String starts with A is correct")
else:
    print("String not starts with A ")

# 8.Write a condition to determine if a person can vote based on their age.
print("\nQuestion8.Write a condition to determine if a person can vote based on their age.")
age=18
if age>=18:
    if age>=21:
        print("You are ready for voting")
    else:
        print("you are elder but not ready for voting")
else:
    print("you are now minor")
# 9.Check if a list is empty or not and print respective messages.
print("\nQuestion9.Check if a list is empty or not and print respective messages.")
list= []
print(f"list={list}")
if not list:
    print("list is empty")
else:
    print("list contain object")
# 10.Verify if a number is divisible by both 3 and 5. If True, print "Divisible by 3 and 5," otherwise print "Not Divisible.
print("\nQuestion10:Verify if a number is divisible by both 3 and 5. If True, print \"Divisible by 3 and 5,\" otherwise print \"Not Divisible.\"")
num=25
print(f"num={num}")
if num % 3==0 and num % 5 ==0:
    print(" Num is Divisible by 3 and 5,")
else:
    print("Num is Not Divisible.")
# ============="if-elif-else Statements===========================================
# 11.Write a program to classify a number as positive, negative, or zero.
print("\nquestion11:Write a program to classify a number as positive, negative, or zero.")

# 12.Create a grading system that prints "A" for marks >= 90, "B" for 75-89, "C" for 50-74, and "Fail" for < 50.
print("\nquestion12:Create a grading system that prints 'A' for marks >= 90, 'B' for 75-89, 'C' for 50-74, and 'Fail' for < 50.")
marks=85
print(f"mark={marks}")
if marks >= 90:
    print("you got an 'A' grade")
elif marks >= 75 and marks <=89:
    print("you got an 'B' grade")
elif marks >= 54 and marks <= 74:
    print("you got an 'c' grade")
else:
    print("You are Fail")
# 13.Check if a number is a single-digit, double-digit, or greater.
print("\nquestion13:Check if a number is a single-digit, double-digit, or greater.")
num=15

# 14.Write a program to determine the type of triangle (equilateral, isosceles, scalene) based on three sides.
triangle={"side1":5,"side2":5,"side3":4}
print(type(triangle))
if triangle["side1"] == triangle["side2"] == triangle["side3"]:
    print("It is an equilateral triangle.")
elif triangle["side1"] == triangle["side2"] != triangle["side3"]:
    print("It is an isosceles triangle.")
else:
    print("It is  scalene triangle.")

# 15.Write a program to classify a year as a leap year or not.
print("\nQuestion15:Write a program to classify a year as a leap year or not.")
year=2016
print(f"year={year}")
if year % 4==0:
    print("year as a leap year")
else:
    print("yesr is not leap year")

# ========================Logical Operators (and, or, not)==========================================
# 16.Check if a number is between 1 and 100 (inclusive).
print("\nQuestion16:Check if a number is between 1 and 100 (inclusive)")
num=1
print(f"num={num}")
if  num >= 1 and num <=100:
    print("a number is between 1 and 100")
else:
    print("a number is not between 1 and 100")

# 17.Write a program to check if a username and password are both correct.
print("\nQuestion17:Write a program to check if a username and password are both correct.")
username=("Snehal")
password=8897
print(f"username={username} and password={password}")
if username=="Snehal" and password==8897 :
    print("a username and password are both correct.")
elif username=="aaaaa" and password==8899:
    print("a username is incorrect")
elif username=="Snehal" and password==8799:
    print("a password is incorrect")
else:
    print("a username and password are both incorrect.")

#18.Verify if a number is divisible by either 2 or 7.
print("\nQuestion18:Verify if a number is divisible by either 2 or 7.")
num=31
print(f"num={num}")
if num %2==0 and num%7!=0:
    print("num is divisable by only 2")
elif num %2 != 0 and num % 7 ==0:
    print("num is divisable by only 7")
elif num %2 ==0 and num %7 ==0:
    print("num is divisible by either 2 or 7")
else:
    print("num is not divisable by either 2 or 7 ")

# 19.Check if a number is not between 50 and 150.
print("\nQuestion19:Check if a number is not between 50 and 150.")
num=70
print(f"num={num}")


# 20.Write a program to determine if a student passes with a minimum of 50 marks in all subjects.
# =================Nested if Statements============================
# 21.Write a program to classify a person as a minor, teenager, or adult based on age.
print("\nquestion21:Write a program to classify a person as a minor, teenager, or adult based on age.")
age=25
print(f"age={age}")
if age>=18:
    if age==18:
        print("you are teenager")
    if age>18:
        print("you are adult")
else:
    print("you are minor")

# 22.Check if a number is divisible by 2, and if so, verify if it is also greater than 10.
print("\nQuestion22.Check if a number is divisible by 2, and if so, verify if it is also greater than 10.")
num=11
print(f"num={num}")
if num >10:
    if num % 2== 0:
        print("num is divisible by 2 and greater than 10 ")
    if num % 2 != 0:
        print("num is not divisible by 2 but greater than 10")
else:
    print("num is less than 10")

# 23.Write a program to check if a string contains a vowel and, if it does, check if it starts with a vowel.
print("\nQuestion23:Write a program to check if a string contains a vowel and, if it does, check if it starts with a vowel.")
string="i love my India"
print(f"string={string}")
if "a"or "e"or "i"or "o" or "u" in string:
    if string.startswith("a"or "e"or "i"or "o" or "u"):
        print("string starts with vowel")
else:
    print("string does not contain vowel")
    
# 24.Verify if a number is divisible by 4 and then check if it is even.
# 25.Write a program to check if a number is prime, using nested if statements.Practical Applications
# 26.Write a program to determine the day of the week based on an integer input (1-7).
# 27.Check if a user-provided temperature is "Cold," "Warm," or "Hot" based on thresholds.
# 28.Write a program to evaluate a person's eligibility for a senior citizen discount (age >= 60).
# 29.Check if a given year and month combination is valid.
# 30.Write a program to check if a file extension is valid for image files (.jpg, .png, .gif).
# #========Advanced Logical Operators======================================
# 31.Verify if a person qualifies for a scholarship: minimum 80% marks and income below a certain threshold.
# 32.Check if a password is both 8 characters or longer and contains a special character.
# 33.Write a program to verify if a number is a 3-digit number and also divisible by 11.
