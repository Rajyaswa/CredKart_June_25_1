#==============================i.Arithmetic Operators
# 1.Define a = 15 and b = 4. What is the result of a + b?
from operator import truediv

a=15
b=4
print(f"The result of a+b =",a+b)

#2.Define x = 20 and y = 5. Calculate x -y and print the result
x=20
y=5
sub=x-y
print(f"result is = ",sub)

#3.Define num1 = 3 and num2 = 7. Calculate the product of num1 and num2.
num1 = 3
num2 = 7
product=num2*num1
print(f"The product of num1 and num2 =",product)

#4.Define dividend = 40 and divisor = 8. What is the result of dividend / divisor?
dividend = 40
divisor = 8
division=40/8
print(f"the result of dividend / divisor =",division)

dividend = 40
divisor = 8
floor_division=40//8
print(f"the result of dividend // divisor =",floor_division)

#5.Using a = 10, calculate a % 3 and explain the result
a = 10
modulus = a % 3
print(modulus) # result should be 1 means modulus operator display the reminder of division operation


#6.Define base = 2 and power = 5. Calculate base ** power
base = 2
power = 5
exponent=base ** power
print("Result of base ** power =",exponent)

#7.Define a = 7 and b = 4. Calculate (a + b) * 2 -b.
a = 7
b = 4
Calculate=(a + b) * 2 -b
print(f"The result of calculation [(a + b) * 2 -b] = ",(a + b) * 2 -b)

#8.Define x = 9 and y = 2. What is the result of x // y?
x = 9
y = 2
Floor_Division= x // y
print(f"the result of x // y = ",Floor_Division)

#9.Calculate 15 + 6 * 2 -4 / 2 and explain the result using operator precedence.
a=15
b=6
c=2
d=2
calculate =15 + 6 * 2 -4 / 2
print(f"result of [15 + 6 * 2 -4 / 2] = ", calculate)
"""in this example  the mathematic operation run as per BODMOS rule 
                        1st action is 6*2=12
                        2nd action is 4/2=2
                        3rd action is 12-2=10
                        last action is 15+10=25 """
#10.Using a = 5 and b = 3, calculate a ** b + a * b -b
a = 5
b = 3
Operation= a ** b + a * b -b
print(f"Result of calculation  a ** b + a * b -b = ",Operation)

#11.Define x = 100 and y = 20. Calculate (x -y) / y.
x = 100
y = 20
sum=(x -y) / y
print(f"The result of (x -y) / y = ",sum)


# 12.Define num = 50. Calculate and print num % 7.
num = 50
print(f"Result of num % 7 =",num % 7)


# 13.Calculate the area of a rectangle with length = 10 and width = 5 using multiplication.
length = 10
width = 5
Area=length * width
print(f"the area of a rectangle =",Area)


# 14.Calculate (10 + 5) * 3 -7 ** 2.15.Using a = 8 and b = 3, find the integer result of a / b.
a = 8
b = 3
print(f"(10 + 5) * 3 -7 ** 2 = ",(10 + 5) * 3 -7 ** 2)
print(f"integer result of a / b = ",a / b)


# 16.Define price = 100 and tax = 0.1. Calculate the total price with tax.
price = 100
tax = 0.1
sum=(price*tax)+price
print(f"the total price with tax is ",sum)

#17.Define a = 9. Calculate and print the square root of a using **.
a = 9
sum=a**0.5
print(f"The square root of 9 =",sum)


# 18.Using x = 4, calculate and print x ** 3 + 2 * x.
x = 4
print(f"The result of [x ** 3 + 2 * x] =",x ** 3 + 2 * x)

# 19.Calculate 20 % 6 and explain what the remainder represents.
a=20
b=6
print(f" Result of 20 % 6 = ",20 % 6) # the amount "left over" after performing some computation

#20.Write a Python program to add two numbers from user input and print the sum




#================================ii.Assignment Operators==================================
#1.Define x = 10. Use += to add 5 to x and print the result.
x=10
x+=5
print(f"x+=5:={x}")

#2.Define y = 20. Use -= to subtract 3 from y.
y=20
y-=3
print(f"y-=3:={y}")

# 3.Define z = 3. Use *= to multiply z by 4 and print the result.
z=3
z*=4
print(f"z*=4 :={z}")
# 4.Using x = 100, divide x by 10 with the /= operator.
x=100
x/=10
print(f"x=100 :={x}")
# 5.Define a = 15. Use %= 4 to get the remainder of a divided by 4.
a=15
a%= 4
print(f"a%= :4={a}")
# 6.Define base = 2. Raise it to 3 using **=.
base = 2
base **=3
print(f"base **=3:={base}")
# 7.Define x = 25. Use //= 5 to find the integer division result and assign it back to x.
x = 25
x//= 5
print(f"x//= 5:={x}")
# 8.Set points = 10. Increase points by 5 using +=.
points = 10
points+=5
print(f"points +=5,:{points}")
# 9.Define counter = 1. Double it using *= and print.
counter = 1
counter *=2
print(f"counter *=2,:{counter}")

# 10.Define price = 100. Apply a 20% discount using -=.
price = 100
price*=20
print(f"result ={price}")
price/=100
print(f"result ={price}")

# 11.Define total = 10. Increase total by 3, then by 2, using assignment operators.
x=10
x+=3
print(f"x+=3 ;={x}")
x+=2
print(f"x+=2 ;={x}")
# 12.Using x = 5, use **= to make it 5 ** 2.
x=5
x**=2
print(f"x**=2 ;={x}")
#13.Set y = 50. Reduce it by 10 using -=.
x=50
x-=10
print(f"x-=10;={x}")
#14.Define z = 8. Multiply it by 2, then divide it by 4 with assignment operators.
z=8
z*=2
print(f"z*=2 ;=,{z}")
z/=4
print(f"z/=2 ;=,{z}")

# 15.Define bonus = 50. Increase it by 10% using +=.
bonus = 50
bonus*=10
print(f"bonus*110 ;={bonus}")
bonus/=100
print(f"bonus*110 ;={bonus}")
bonus += 50
print(f"bonus += 50 ;= {bonus}")

# 16.Define score = 5. Subtract 2 using -=.
score = 5
score-=2
print(f"score-=2 :={score}")

# 17.Define num = 6. Add 4, then multiply by 2 using assignment operators.
num = 6
num+=4
print(f"num+=4 ;={num}")
num*=2
print(f"num*=2 ;={num}")

# 18.Using x = 30, reduce x by 5, then increase by 10.
x=30
x-=5
print(f"x-=5 ;={x}")

# 19.Set initial = 100. Halve it using //=.
initial = 100
initial //= 2
print(f"initial //= 2;={initial}")

# 20.Define time = 20. Reduce it by 25% using assignment operators.
time=20
time*=25/100
print(f"time*=25/100;= {time}")
time=20
time-=5
print(f"time-=5;= {time}")


#========================================iii.Comparison Operators================================================
# 1.Define x = 10 and y = 15. Check if x == y.
x = 10
y = 15
print(f"for x = 10 and y = 15 then x == y ;={x == y}")
# 2.Check if x != y for x = 20 and y = 20.
x = 20
y = 20
print(f"for x = 20 and y = 20 then x != y ;={x != y}")

# 3.Using age1 = 18 and age2 = 21, check if age1 < age2.
age1 = 18
age2 = 21
print(f"age1 = 18 and age2 = 21 then age1 < age2 ;={age1 < age2}")

# 4.Define height1 = 170 and height2 = 165. Check if height1 > height2.
height1 = 170
height2 = 165
print(f"height1 = 170 and height2 = 165 then height1 > height2 ;= {height1 > height2}")

# 5.Define a = 5 and b = 5. Check if a <= b.
a = 5
b = 5
print(f"a = 5 and b = 5 then a <= b;={a <= b}")
# 6.Using score1 = 90 and score2 = 85, check if score1 >= score2.
score1 = 90
score2 = 85
print(f"score1 = 90 and score2 = 85 then score1 >= score2 = {score1 >= score2}")

# 7.Define a = 10, b = 5, and c = 15. Check if a + b == c.
a = 10
b = 5
c = 15
print(f"a = 10, b = 5, and c = 15 then ={a + b == c}")

# 8.Using temp = 100, check if temp == 100.
temp = 100
print(f"temp = 100, if temp == 100 then  ={ temp == 100}")
# 9.Define num = 50. Check if num < 100.
num = 50
print(f"if num < 100;={num < 100}")
# 10.Define x = 5. Check if x >= 3 and x <= 10.
x = 5
print(f"if x >= 3 and x <= 10 then ;={x >= 3,x <= 10}")
#11.Define a = 12 and b = 6. Check if a > b and b < 10.
a = 12
b = 6
print(f"is a > b and b < 10 ;={a > b, b < 10}")
# 12.Check if x == 10 or x == 20 for x = 15.
x = 15
print(f" x == 10 or x == 20 then;= {x == 10 , x == 20} ")

# 13.Check if 5 + 5 == 10 and 10 -3 == 7.
print(f" 5 + 5 == 10 and 10 -3 == 7 is{ 5 + 5 == 10 , 10 -3 == 7}")

# 14.Define a = 8. Check if a ** 2 > 50.
a=8
print(f"a ** 2 > 50 is ;={a ** 2 > 50}")
# 15.Define age = 25. Check if age != 30.
age = 25
print(f" condition age != 30 is;={age != 30}")

# 16.Define score = 100. Check if score >= 90.
score = 100
print(f"the condition score >= 90 is:= {score >= 90}")
# 17.Define num = 5. Check if num == 5 and num < 10.
num = 5
print(f"condition num == 5 and num < 10 is :=,{num == 5 , num < 10}")
# 18.Using x = 3, check if x < 5 or x > 10.
x = 3
print(f" condition x < 5 or x > 10 is ;= {x < 5 , x > 10}")

# 19.Define speed = 80. Check if speed == 80.
speed = 80
print(f"condition speed == 80 is := {speed == 80}")

# 20.Define mark = 60. Check if mark <= 50 or mark >= 60.
mark = 60
print(f"if mark <= 50 or mark >= 60 then ;={mark <= 50 ,mark >= 60}")


###=================iv.Logical Operators=================================================
# 1.Define a = True and b = False. Check a and b.
a = True
b = False
print(f"a and b: {a and b}")
# 2.Define p = True and q = True. Check p and q.
p = True
q = True
print(f"p and q: {p and q}")
# 3.Using r = False and s = True, check r or s.
r = False
s = True
print(f"check r or s ;={ r or s}")

# 4.Define x = True. Check not x.
x=True
print(f"check not x ;={not x}")

# 5.Check if True and False.
print(f"True and False;{True and False}")

# 6.Define p = True. Check if not p.
p = True
print(f"if not p:{not p}")

# 7.Define a = 10 and b = 5. Check (a > b) and (b < 10).
a = 10
b = 5
print(f"Check (a > b) and (b < 10) ;={ (a > b) and (b < 10)}")
#8.Define num = 20. Check (num > 15) or (num < 10).
num = 20
print(f"(num > 15) or (num < 10);={(num > 15) or (num < 10)}")

# 9.Check if not (10 > 5).
print(f"if not (10 > 5)'={ not (10 > 5)}")

# 10.Using age = 30, check (age >= 20) and (age <= 40).
age = 30
print(f"check (age >= 20) and (age <= 40) ;={(age >= 20) and (age <= 40)}")

# 11.Using x = 5, check (x == 5) or (x == 10).
x = 5
print(f"check (x == 5) or (x == 10)'={(x == 5) or (x == 10)}")

# 12.Define status = True. Check if status and not status.
status = True
print(f"Check if status and not status =; { status and not status}")

# 13.Define a = 4 and b = 4. Check (a == b) and (a < 10).
a=4
b=4
print(f"(a == b) and (a < 10) :={(a == b) and (a < 10)}")

# 14.Check not (False or True).
print(f"not (False or True) ;={not (False or True)}")

# 15.Define y = 7. Check y > 5 and y < 10.
y=7
print(f"y > 5 and y < 10 :={y > 5 and y < 10.}")

# 16.Using temp = 50, check if temp > 60 or temp == 50.
temp = 50
print(f"temp > 60 or temp == 50 := {temp > 60 or temp == 50}")

# 17.Define a = 10. Check if a > 5 or a < 5.
a = 10
print (f"a > 5 or a < 5 ;={a > 5 or a < 5}")

# 18.Define num = 8. Check (num == 8) and (num > 5).
num = 8
print(f"(num == 8) and (num > 5) ;={(num == 8) and (num > 5)}")

# 19.Check if not (5 < 3).
print(f"not (5 < 3) ;={not (5 < 3)}")

# 20.Using x = True and y = False, check (x and y) or (not y).
x = True
y = False
print(f"(x and y) or (not y) :={(x and y) or (not y)}")

##===============v.Membership and Identity Operators===============================================
# 1.Define a list colors= ["red", "blue", "green"]. Check if "blue" is in colors.
list = ["red", "blue", "green"]
print(f" blue is in colors :{'blue' in list}")

# 2.Define fruits = ["apple", "banana"]. Check if "grape" is not in fruits.
fruits = ["apple", "banana"]
print(f"grape is not in fruits := {'grape' not in fruits}")

# 3.Define x = 10 and y = 10. Check if x is y.
x = 10
y = 10
print(f"if x is y ;={ x is y}")

# 4.Define a = [1, 2] and b = [1, 2]. Check if a is b.
a = [1, 2]
b = [1, 2]
print(f"if a is b :={ a is b}")

#5.Using name = "John", check if "o" is in name.
name = "John"
print(f"o is in name :={'o'in name}")

# 6.Define cities = ["NY", "LA", "SF"]. Check if "LA" is in cities.
cities = ["NY", "LA", "SF"]
print(f"LA is in cities ;={'LA'in cities}")

# 7.Using numbers = [1, 2, 3, 4], check if 5 is not in numbers.
numbers = [1, 2, 3, 4]
print(f"5 is not in numbers :={5 not in numbers}")

# 8.Define x = 20. Check if x is not 10.
x = 20
print(f"x is not 10 :={x is not 10}")

# 9.Define list1 = [1, 2] and list2 = list1. Check if list1 is list2.
list1 = [1, 2]
list2 = list1
print(f"list1 is list2 ;={list1 is list2}")

# 10.Define a = 5 and b = 5. Check if a is b.
a = 5
b = 5
print(f"a is b :={a is b}")

# 11.Define name = "Alice". Check if "A" is in name.
name = "Alice"
print(f"A is in name := {'A' in name}")

# 12.Using letters = ["a", "b", "c"], check if "d" is not in letters.
letters = ["a", "b", "c"]
print(f"d is not in letters := {'d'  not in letters}")

# 13.Define x = 30. Check if x is not 20.
x = 30
print(f"x is not 20 ;={x is not 20}")

# 14.Using fruit = "apple", check if "p" is in fruit.
fruit = "apple"
print(f"p is in fruit :={'p' in fruit}")

# 15.Define list1 = [1, 2] and list2 = [1, 2]. Check if list1 is list2.
list1 = [1, 2]
list2 = [1, 2]
print(f"list1 is list2 :={list1 is list2}")

# 16.Define x = "hello". Check if "e" in x.
x = "hello"
print(f"e in x :={'e' in x}")

# 17.Define num = 10. Check if num is 10.
num = 10
print(f"if num is 10:={ num is 10}")

# 18.Using colors = ["red", "blue"], check if "green" not in colors.
colors = ["red", "blue"]
print(f"green not in colors :={'green'not in colors}")

# 19.Define word = "python". Check if "py" in word.
word = "python"
print(f"py in word:={'py' in word} ")

# 20.Using name = "Anna", check if "a" is in name (case-sensitive check).
name = "Anna"
print(f"a is in name := {'a'in name}")


