#=====================Basic List Concepts===========================================
# 1.What is a list in Python, and how is it defined?
'''A list is defined using square brackets [], and the elements are separated by commas.'''
#Ordered: Elements have a specific order that does not change unless you modify it.
#Mutable: You can change, add, or remove elements.
#Indexed: Elements can be accessed by their index (starting from 0)

# 2.Can lists in Python contain different data types? Provide an example.
'''Yes, lists in Python can contain different data types all together in the same list.'''
my_list = [42, "hello", 3.14, True, [1, 2, 3]]
print(my_list)

# 3.How do you create an empty list in Python?
my_list = []
my_list = list()

# 4.How does list concatenation work, and how can you concatenate two lists?
'''List concatenation means joining two or more lists into a single list. 
It creates a new list containing all the elements from the original lists in the same order.'''

# 5.Explain list repetition. How do you repeat the elements of a list multiple times?List Operations
'''List repetition means repeating the elements of a list multiple times. 
This is done using the * operator.'''
#new_list = original_list * n

# 6.What is list indexing, and how can you access the first and last elements of a list?
'''List indexing is the method used to access individual 
elements of a list using their position (index).'''
#Indexing starts at 0 for the first element.
#Negative indexes start at -1 for the last element.

# 7.How does list slicing work, and how can you slice a list to get items from index 1 to 3?
'''List slicing lets you extract a portion (sublist) of a list using a range of indexes.'''
#sublist = list[start:stop]
#start → index to begin (inclusive)
#stop → index to end (exclusive)
#It includes elements from start up to but not including stop.

#| Slice Expression | Description                  |
#| ---------------- | ---------------------------- |
#| `my_list[:]`     | Entire list                  |
#| `my_list[:3]`    | First 3 elements (0 to 2)    |
#| `my_list[2:]`    | From index 2 to the end      |
#| `my_list[-3:-1]` | 3rd last to 2nd last element |

# 8.How do you check if an element exists in a list using the membership operator?
'''You can use the membership operator in to check if an element exists in a list.'''
#element in list
'''To check if an element does not exist in a list, use not in'''
#print('grape' not in fruits)  # Output: True

# 9.How can you find the length of a list?
'''You can find the length of a list in Python using the built-in len() function. Here's how you use it:'''
#my_list = [1, 2, 3, 4, 5]
#length = len(my_list)
#print(length)  # Output: 5

# 10.How can you count the occurrences of a specific element in a list?
'''You can count the occurrences of a specific element in a list using the .count() method. '''
#my_list = [1, 2, 2, 3, 2, 4, 5]
#count_of_2 = my_list.count(2)
#print(count_of_2)  # Output: 3

# ====================List Methods===================================================================
# 11.What is the purpose of the append() method, and how is it used?
'''The append() method in Python is used to add a single element to the end of a list.'''
#list_name.append(element)

# 12.How does the insert() method work, and how can you insert an element at a specific position
'''The insert() method in Python is used to insert an element at a specific index in a list.'''
#index is the position where you want to insert the element.
#element is the value to insert.

#How it works:
#It shifts the existing elements to the right from the specified index.
#The list grows by one element.
numbers = [10, 20, 30, 40]
numbers.insert(2, 25)
print(numbers)  # Output: [10, 20, 25, 30, 40]

#13.Describe the remove() method and explain what happens if the element is not found.
'''The remove() method in Python is used to remove the first occurrence of a 
specified element from a list.'''
#element is the value you want to remove.
#It removes only the first matching element.
#The original list is modified in place.

fruits = ['apple', 'banana', 'orange', 'banana']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'orange', 'banana']


# 14.How does the pop() method work, and what does it return?
'''The pop() method in Python is used to remove and return an element from a list.'''
#index is optional. If provided, pop() removes and returns the element at that position.
#If no index is given, it removes and returns the last element.
fruits = ['apple', 'banana', 'orange']
last_item = fruits.pop()
print(last_item)   # Output: 'orange'
print(fruits)      # Output: ['apple', 'banana']

fruits = ['apple', 'banana', 'orange']
item = fruits.pop(1)
print(item)        # Output: 'banana'
print(fruits)      # Output: ['apple', 'orange']


# 15.What does the clear() method do to a list?
'''The clear() method in Python is used to remove all elements from a list, making it empty.'''

fruits = ['apple', 'banana', 'orange']
fruits.clear()
print(fruits)  # Output: []

# =========Sorting and Reversing==================================================================

# 16.How can you sort a list in ascending order using a method?
'''You can sort a list in ascending order using the sort() method in Python.'''
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 7, 9]
#sort() modifies the original list.
#By default, it sorts in ascending order.
#If you want descending order, use:

# 17.How can you reverse the order of elements in a list?
'''You can reverse the order of elements in a list using the reverse() method.'''
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]

# 18.What is the difference between sort() and sorted() in Python?
#sort() method
#Used on lists only.
#Modifies the original list in place (does not create a new list).
#Returns None.
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

#sorted() function
#Works on any iterable (lists, tuples, strings, etc.).
#Returns a new sorted list, leaving the original unchanged.
numbers = [3, 1, 4, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4]
print(numbers)         # Original list unchanged: [3, 1, 4, 2]

# ============================Advanced List Operations====================================================
# 19.How do you find the maximum and minimum values in a list of numbers?
#You can find the maximum and minimum values in a list of numbers using the built-in Python functions:
#max() — returns the largest value
#min() — returns the smallest value
numbers = [10, 25, 7, 99, 3]
maximum_value = max(numbers)
minimum_value = min(numbers)
print("Max:", maximum_value)  # Output: Max: 99
print("Min:", minimum_value)  # Output: Min: 3

# 20.What is list comprehension, and how is it used to generate a list of squares?
'''List comprehension is a concise and readable way to create lists in Python by embedding 
a for loop and optional conditions inside square brackets.'''
#Purpose:
#To generate a new list by applying an expression to each item in an existing iterable (like a list or range).
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# 21.How can you create a list of even numbers using list comprehension?
'''You can create a list of even numbers using list comprehension by including a 
condition that checks if each number is even.'''
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 22.How does the extend() method differ from append() when adding elements to a list?
''' Both append() and extend() are used to 
add elements to a list in Python, but they behave differently'''
# append()
#Adds a single element to the end of the list.
#If you pass a list, it adds the entire list as a single element (nested list).
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # Output: [1, 2, 3, [4, 5]]
'''extend()
Adds each element of an iterable (like a list, tuple, etc.) to the end of the list.
If you pass a list, it adds each element individually.'''
list1 = [1, 2, 3]
list1.extend([4, 5])
print(list1)  # Output: [1, 2, 3, 4, 5]

# 23.Explain how to find the index of an element in a list.
'''To find the index of an element in a list in Python, you use the index() method.'''
#Returns the first index of the specified element.
#Raises a ValueError if the element is not in the list.
numbers = [10, 20, 30, 40, 30]
print(numbers.index(30))  # Output: 2

# ===================Working with Nested Lists=================================
# 24.What is a nested list, and how do you access elements in a nested list?
'''A nested list is a list that contains other lists as elements. It’s like a list inside another list.'''
nested = [[1, 2], [3, 4], [5, 6]]
print(nested[0])      # Output: [1, 2]     (first inner list)
print(nested[0][1])   # Output: 2         (second element in first inner list)
print(nested[2][0])   # Output: 5         (first element in third inner list)

# 25.How can you flatten a nested list (turn a 2D list into a 1D list)?
nested = [[1, 2], [3, 4], [5, 6]]
flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)  # Output: [1, 2, 3, 4, 5, 6]


# ===========================Copying Lists and List Conversion===============================

# 26.What is a shallow copy of a list, and how can you create one?
'''A shallow copy of a list is a new list object that contains references 
to the same elements as the original list. In other words:
The outer list is copied, but
The inner objects (like sublists or other mutable elements) are not duplicated, just referenced.'''


# 27.How do you convert a string to a list of characters, and vice versa?
text = "hello"
char_list = list(text)
print(char_list)  # Output: ['h', 'e', 'l', 'l', 'o']


# 28.How can you delete specific elements from a list using del?
'''You can use the del statement in Python to delete specific 
elements from a list by their index or range of indexes.'''
fruits = ['apple', 'banana', 'cherry']
del fruits[1]
print(fruits)  # Output: ['apple', 'cherry']


# =============Iteration and Built-in Functions===========================

# 29.How do you iterate over a list and print each element using a for loop?
'''To iterate over a list and print each element using a for loop in Python, 
you simply loop through the list directly.'''
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit) #apple,banana,cherry

# 30.How can you use the enumerate() function to get both the index and the value of each element in a list?
'''The enumerate() function in Python allows you to loop through a list and get both the index and 
the value of each element at the same time — which is super handy!'''
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
    #output
#Index 0: apple
#Index 1: banana
#Index 2: cherry
