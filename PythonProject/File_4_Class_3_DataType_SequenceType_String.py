a="My name is snehal,I'm from Kolhapur"
print(a)
print(type(a))
print("data type of a is",type(a))
S1= "My name is Snehal"
S2="""Now I'm learning a Software testing class"""
S3="to move forward in IT sector"
print(S1,"\n",S2,"\n",S3)
print(S1,",",S2,",",S3,".")
print(S1+", "+S2)
print((S1+"\n")*6)
#S1= "My name is Snehal"
print(S1[4])
print(S1[-9])
print(S1[2:7])
print(S1[-7:-1])
print(len(S1))
print(S1.upper())
print(S2.lower())
print(S1.title())
print(S1.swapcase())
print(S1.replace("My name is Snehal","i am snehal"))
print(S1.find("m"))
print(S1.count("m"))
print(S1.split())
print(S2.split(" "))
print(S1.startswith("i"))
print(S1.endswith("l"))
print(S1.index("m"))
print("i"in S1)
# String Formatting
print("\n 05. String Formatting : ")
name = "Vijay"
age = 21


print("My name is {} and my age is {}".format(name, age)) # old way
print("My name is {0} and my age is {1}".format(name, age))# old way
print("My name is {name} and my age is {age}".format(name=name, age=age))# old way

name=("snehal")
age=32
print("My name is {} and My age is {}".format(name,age))
print("My name is {0} and my age is {1}".format(name, age))# old way

print("My name is", name, "and my age is", age) # New way
print(f"My name is {name} and my age is {age}") # f string new way, famous one