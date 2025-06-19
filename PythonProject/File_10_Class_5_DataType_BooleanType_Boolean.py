# Data Type : Boolean --> Boolean is a data type which is either True or False.


# 01. Boolean
print("01. Boolean : ")
bool1= True
bool2 = False
print("The data type of a is", type(bool1))


# 02. Example of Boolean
print("\n02. Example of Boolean : ")
print(bool1)
print(bool2)


# 03. Operations with Boolean
print("\n03. Operations with Boolean : ")
print(bool1 and bool2) # False
print(bool1 or bool2) # True
print(not bool1) # False


"""
True and True = True
True and False = False
False and True = False
False and False = False

True or True = True
True or False = True
False or True = True
False or False = False

not True = False
not False = True
"""


# all and any
print("\n04. all and any : ")
print(all([True, True, False])) # all() returns True if all items in list are True
#Output : False
print(all([True, True, True])) # all() returns True if all items in list are True
#Output : True
print(any([True, True, False])) # any () returns True if any item in list is True
#Output : True
print(any([False, False, False])) # any () returns True if any item in list is True
#Output : False

print("\n05. Boolean Conversion : ")
print(bool("Hello")) # True # string
print(bool(" ")) # True # string
print(bool("")) # False # empty string
print(bool(1)) # True # integer
print(bool(4)) # True # integer
print(bool(0)) # False #integer


# Most used data type in python selenium pytest framework
# 1. String
# 2. Integer
# 3. Float
# 4. Boolean
# 5. List