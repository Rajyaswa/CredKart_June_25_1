#==========Basic String Concepts=========
# 1.What is a string in Python, and how is it defined?
#In Python, a string is a sequence of characters used to represent text such as words,sentences, or symbols.
#Strings can include:Letters (a–z, A–Z),Numbers (0–9),Symbols (!, @, #, etc.)
#Spaces and other special characters
#Strings are enclosed in quotes:Single quotes,Double quotes,Triple quotes
#Strings are immutable (they cannot be changed after creation).

# 2.How can you create a multiline string in Python?
#we can create a multiline string in Python using triple quotes — either ''' (single) or """ (double) """

# 3.What is the difference between using single (' ') and double (" ") quotes for strings in Python?
#There is no functional difference between single and double quotes in Python. Both define a string.

# 4.What is the purpose of escape characters in strings, and give three examples.
#To insert special characters or avoid errors when dealing with characters like quotes, newlines, tabs, etc.

#5.What is string concatenation, and how do you concatenate two strings?
#String concatenation means joining two or more strings together to make a new, longer string.
#the plus operator (+) to join strings
#print(s1 + " " + s2) # Concatenation


#================ String Operations===================================================================
# 6.Explain string repetition and provide an example.
"""String repetition means creating a new string by repeating the same string multiple times.
multiplication operator (*) with a string and an integer"""
string = "Hello"
string_repetition = string * 3
print(string_repetition)

# 7.What does string indexing mean, and how can you access the first and last characters of a string?
'''String indexing means accessing individual characters in a string by their position (index).
Python strings are like lists of characters.
Each character has an index starting at 0 for the first character.
Negative indexes count from the end (-1 is the last character).'''

# 8.How does string slicing work, and how would you slice a string from index 1 to 4?
'''String slicing lets you extract a part of the string by specifying a range of indexes.'''
s1 = "Credence"
#print(s1[1:4]) #slicing

# 9.Explain the concept of membership in strings. How can you check if a character is in a string?
#Membership refers to checking if a character or substring exists within another string.
s1 = "Credence"
print("Membership : ", "C" in s1) # True
print("Membership : ", "T" in s1) # True

# 10.How can you find the length of a string?
s1 = "Credence"
print(len(s1)) # length of string

#=========================String Methods================================================================
# 11.What is the purpose of the .lower() and .upper() methods in strings?
'''These methods are used to change the case (uppercase or lowercase) of letters in a string.'''
s1 = "Credence"
print("Convert to uppercase : ", s1.upper())
print("Convert to lowercase : ", s1.lower())

#12.How does the .replace() method work, and give an example of replacing a character in a string.
#The .replace() method is used to replace a specific substring or character in a string with another value.
s1 = "Credence"
print("Replace : ", s1.replace("Credence", "Automation Testing"))

# 13.Describe the .split() method and explain what it returns.
'''The .split() method is used to split a string into a list of substrings, based on a separator (delimiter).'''
s2 = "Automation Testing"
print("Split : ", s2.split(" ")) # list

# 14.What does the .strip() method do, and when might you use it?
'''The .strip() method is used to remove unwanted characters (by default, spaces) from the beginning and end of a string.'''

# 15.How can you find the position of the first occurrence of a substring in a string using a method?String Formatting.
'''To find the position (index) of the first occurrence of a substring, you can use:'''
string.find(substring)

# 16.What are the different methods of formatting strings in Python? Give examples for format(), f-strings, and % formatting.
# String Formatting
print("\n 05. String Formatting : ")
name = "Vijay"
age = 21
print("My name is {} and my age is {}".format(name, age)) # old way

name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old.")

name = "Carol"
age = 28
print("My name is %s and I am %d years old." % (name, age))

#| Method         | Syntax Example             | Notes                                   |
#| -------------- | -------------------------- | --------------------------------------- |
#| `format()`     | `"Hello, {}".format(name)` | Works in Python 2 & 3                   |
#| `f-string`     | `f"Hello, {name}"`         | Most readable & powerful (3.6+)         |
#| `%` formatting | `"Hello, %s" % name`       | Old style; not recommended for new code |


# 17.How do you use f-strings to embed variables directly in a string?
'''f-strings (formatted string literals) allow you to embed variables and expressions directly 
inside a string using curly braces {}.'''
name = "Alice"
print(f"Hello, {name}!")  # Output: Hello, Alice!

# 18.Describe how to use the .format() method for string formatting with an example.
'''The .format() method allows you to insert values into a string using curly braces {} as placeholders.'''
name = "Alice"
age = 25

sentence = "My name is {} and I am {} years old.".format(name, age)
print(sentence)
# Output: My name is Alice and I am 25 years old.

#==========================# Escape Characters=================================
# 19.What is an escape character, and why would you use it?
'''An escape character is a special character used in strings to represent characters that are hard 
to type or have special meaning in code.
It starts with a backslash \ followed by another character.
It tells Python to interpret the next character differently.'''
'''To include special characters like newlines, tabs, or quotes inside strings without causing errors.
To insert characters that can’t be typed directly or would otherwise be interpreted as code.'''

# 20.How do you add a newline within a string using escape sequences?
'''To insert a newline (line break) inside a string, use the escape character \n.'''
text = "Hello\nWorld"
print(text)

# 21.Give an example of using an escape character for including a backslash within a string.
'''Since the backslash \ is used to start escape sequences, to include an actual backslash in a string, 
you escape the backslash itself by typing \\.'''
path = "C:\\Users\\Alice\\Documents"
print(path)


# ==========================Raw Strings and Joining======================================
# 22.What is a raw string, and how does it differ from a regular string?
'''A raw string is a string literal prefixed with an r or R (e.g., r"text"). 
In raw strings, escape sequences are not processed — backslashes are treated as literal characters.'''
#To write Windows paths without doubling backslashes:
path = r"C:\Users\Alice\Documents"
print(path)  # Output: C:\Users\Alice\Documents
#To write regular expressions easily without worrying about escaping backslashes.

# 23.How do you convert a list of strings into a single string with spaces between each word?
'''To convert a list of strings into a single string with spaces between each word, you can use the .join() method.'''
words = ["Hello", "world", "this", "is", "Python"]
sentence = " ".join(words)
print(sentence)

#24.What does the .join() method do, and how is it used to create a hyphen-separated string?
# ================Advanced String Methods=============================
# 25.What does the .capitalize() method do to a string?
'''The .capitalize() method returns a copy of the string where:
The first character is converted to uppercase.
All other characters are converted to lowercase.'''
text = "hELLO world"
print(text.capitalize())## output -Hello world

# 26.How does .swapcase() work on a string with both uppercase and lowercase characters?
'''The .swapcase() method returns a new string where:
All uppercase letters are converted to lowercase.
All lowercase letters are converted to uppercase.
It swaps the case of every letter in the string.'''
text = "Hello World!"
swapped = text.swapcase()
print(swapped)
#output= hELLO wORLD!

# 27.Explain the use of the .zfill() method with an example.
'''The .zfill(width) method pads a numeric string on the left with zeros (0) until 
it reaches the specified total length (width).'''
#Used to format numbers as strings with leading zeros.
#Helpful for things like IDs, codes, or aligning numbers.
num_str = "42"
padded = num_str.zfill(5)
print(padded) # output=00042

# 28.What is the purpose of .center(), .ljust(), and .rjust() in formatting strings?
#Method	                      What It Does	                                 Example
#.center()	 Centers the string within a specified width        	"Hello".center(11) → ' Hello '
#.ljust()	 Left-justifies (aligns left) within the width	         "Hello".ljust(11) → 'Hello '
#.rjust()	 Right-justifies (aligns right) within the width	     "Hello".rjust(11) → ' Hello'


# ============Converting Between Strings and Lists======================================
# 29.How can you convert a string into a list of individual characters?
'''You can convert a string into a list of its characters by simply using the list() function.'''
text = "Hello"
char_list = list(text)
print(char_list) #output =['H', 'e', 'l', 'l', 'o']

# 30.Once you have a list of characters, how can you convert it back into a single string?
'''Use the ''.join() method to join the list elements into one string.'''
char_list = ['H', 'e', 'l', 'l', 'o']
text = ''.join(char_list)
print(text)# output =Hello





