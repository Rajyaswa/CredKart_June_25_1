#================Basic Tuple Concepts==========================================
# 1.What is a tuple in Python, and how is it defined?
'''A tuple in Python is an ordered, immutable collection of elements. That means:'''''
#The order of items is preserved.
#You cannot change (add, remove, or update) items once the tuple is created.
tuple = (1, 2, 3)

# 2.How are tuples different from lists in Python?
#| Feature               | Tuple                                   | List                                |
#| --------------------- | --------------------------------------- | ----------------------------------- |
#| **Mutability**        | Immutable (cannot be changed)           | Mutable (can be changed)            |
#| **Syntax**            | Defined with parentheses `()` or commas | Defined with square brackets `[]`   |
#| **Performance**       | Faster (because immutable)              | Slower compared to tuples           |
#| **Methods available** | Fewer methods (no append, remove)       | Many methods (append, remove, etc.) |
#| **Use case**          | Fixed data, constant collections        | Collections that change over time   |
#| **Memory usage**      | Uses less memory                        | Uses more memory                    |

# 3.Can tuples in Python contain different data types? Provide an example.
'''Tuples in Python can contain different data types all together in the same tuple!'''
my_tuple = ("Alice", 30, 5.5, True)
print(my_tuple)

# 4.How do you create an empty tuple in Python?
empty_tuple = ()

# 5.How does tuple concatenation work, and how can you concatenate two tuples?
'''Tuple concatenation means joining two or more tuples to create a 
new tuple containing all their elements in order.'''
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# =====================Tuple Operations=============================================
# 6.What is tuple indexing, and how can you access the first and last elements of a tuple?
'''Tuple indexing is the way to access individual elements inside a tuple using their position (index).'''
my_tuple = ('a', 'b', 'c', 'd')
print(my_tuple[0])  # Output: 'a'

# 7.How does tuple slicing work, and how can you slice a tuple to get items from index 1 to 3?
'''Tuple slicing works the same way as list slicing — it lets you extract a subset of 
elements from a tuple by specifying a start and end index'''
my_tuple = ('a', 'b', 'c', 'd', 'e')

slice_tuple = my_tuple[1:4]  # index 1 to 3 (4 is excluded)
print(slice_tuple)            # Output: ('b', 'c', 'd')

# 8.How do you check if an element exists in a tuple using the membership operator?
'''You can check if an element exists in a tuple using the membership operator in.'''
my_tuple = (10, 20, 30, 40)

print(20 in my_tuple)  # Output: True
print(50 in my_tuple)  # Output: False

# 9.How can you find the length of a tuple?
'''To find the length of a tuple (i.e., the number of elements it contains), 
you use the built-in len() function.'''
my_tuple = (10, 20, 30, 40)
print(len(my_tuple))  # Output: 4

# 10.How can you count the occurrences of a specific element in a tuple?
'''You can count how many times a specific element appears in a tuple using the count() method.'''
my_tuple = (1, 2, 3, 2, 2, 4, 5)
count_2 = my_tuple.count(2)
print(count_2)  # Output: 3

# ==============================Tuple Methods=======================================
# 11.What is the purpose of the count() method in tuples, and how is it used?
'''The purpose of the count() method in tuples is to find out how many 
times a specific element appears in the tuple.'''
fruits = ('apple', 'banana', 'apple', 'cherry', 'banana', 'apple')
apple_count = fruits.count('apple')
print(apple_count)  # Output: 3

# 12.How does the index() method work in tuples, and how can you find the index of a specific element?
'''The index() method in tuples is used to find the position 
(index) of the first occurrence of a specified element.'''
my_tuple = ('a', 'b', 'c', 'b', 'd')
index_b = my_tuple.index('b')
print(index_b)  # Output: 1

#13.Can you add or remove elements from a tuple? Why or why not?
'''No, you cannot add or remove elements from a tuple in Python. 
This is because tuples are immutable data structures.'''
#Why?
'''Immutable means once a tuple is created, its size and contents cannot be changed.
You cannot modify, add, or delete elements from it.'''
#This is different from lists, which are mutable and allow adding, removing, or changing elements.
'''If you need to add or remove elements, you would typically convert the tuple to a 
list, modify it, and then convert it back to a tuple if needed.'''

#14.How do you create a tuple with a single element, and why is it necessary to use a comma?
'''To create a tuple with a single element, you must include a comma after the element inside the parentheses. 
The comma is necessary because without it, Python will not recognize it as a tuple—it will just treat 
the value inside the parentheses as a regular expression or data type.'''

#Why is the comma necessary?
'''The parentheses alone aren't enough to define a tuple; they can also be used just for grouping expressions.
The comma tells Python, "This is a tuple, even if there’s only one element.'''

a = (5)    # This is just the integer 5, not a tuple
b = (5,)   # This is a tuple with one element: 5

print(type(a))  # <class 'int'>
print(type(b))  # <class 'tuple'>

#15.Can tuples contain other tuples as elements, and how would you access elements in a nested tuple?
'''Yes, tuples can contain other tuples as elements. This is called a nested tuple.'''
nested_tuple = (1, 2, (3, 4, 5), 6)

# ============Converting Between Tuples and Other Data Types========================================
#16.How do you convert a tuple to a list, and why might you do this?
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]

#Why might you do this?
'''Tuples are immutable, meaning you cannot modify them (no adding, removing, or changing elements)'''
'''Lists are mutable, so if you want to change the contents (add, remove, or update elements), 
converting to a list allows you to do that.'''
'''After modifying, if you want an immutable sequence again, you can convert the list back to a tuple.'''

# 17.How do you convert a list to a tuple?18.Can you sort the elements of a tuple? If so, how?
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)
#Can you sort the elements of a tuple? If so, how?
'''Tuples themselves are immutable, so you cannot sort a tuple in place like you can with a list.'''
#However, you can create a new sorted tuple by:
#1.Converting the tuple to a list
#2.Sorting the list
#3.Converting it back to a tuple


# 19.How do you check if all elements in a tuple are true using a built-in function?
#You can check if all elements in a tuple are true by using the built-in Python function all().
#How all() works:
#1.It returns True if every element in the iterable (like a tuple) is truthy (i.e., evaluates to True).
#2.If any element is falsy (False, 0, None, '', etc.), it returns False.
t = (1, True, "hello", [1, 2])
print(all(t))  # Output: True, since all elements are truthy

t2 = (1, 0, "hello")
print(all(t2))  # Output: False, because 0 is falsy


# 20.How can you check if any element in a tuple is true using a built-in function?
'''To check if any element in a tuple is true, you can use the built-in Python function any().'''
#How any() works:
'''It returns True if at least one element in the iterable (like a tuple) is truthy.'''
'''It returns False only if all elements are falsy (False, 0, None, '', etc.).'''
t = (0, False, "", 5)
print(any(t))  # Output: True, because 5 is truthy

t2 = (0, False, "")
print(any(t2))  # Output: False, all elements are falsy


# =========Tuple Packing and Unpacking==============================
# 21.What is tuple packing, and how is it done in Python?
'''Tuple packing is the process of grouping 
multiple values into a single tuple automatically by Python, without explicitly using parentheses.'''

'''You just assign multiple values separated by commas to a single
variable, and Python packs them into a tuple.'''

packed_tuple = 1, 2, 3, "hello"
print(packed_tuple)          # Output: (1, 2, 3, 'hello')
print(type(packed_tuple))    # Output: <class 'tuple'>


# 22.What is tuple unpacking, and how can it be used to assign values to multiple variables?
'''Tuple unpacking is the process of extracting the values from a tuple and 
assigning them to multiple variables in a single statement.'''

'''You write a tuple (or any iterable) on the right side and a matching number of variables on the left side separated by 
commas. Python automatically assigns each element from the tuple to the corresponding variable.'''

my_tuple = (10, 20, 30)

a, b, c = my_tuple

print(a)  # 10
print(b)  # 20
print(c)  # 30

# 23.How would you swap the values of two variables using tuple packing and unpacking?
'''You can swap the values of two variables in Python very elegantly using tuple packing 
and unpacking — without needing a temporary variable.'''
a = 5
b = 10

a, b = b, a

print(a)  # Output: 10
print(b)  # Output: 5



# 24.Can you use tuples as keys in a dictionary? Why or why not?
'''Yes, you can use tuples as keys in a dictionary, but only if the tuples themselves are immutable 
(which they are by default) and contain only immutable elements.'''
#Why?
#1.Dictionary keys must be hashable (immutable and have a fixed hash value).
#2.Tuples are immutable and hashable, so they can be dictionary keys.
#3.But if a tuple contains any mutable elements like lists or other dictionaries,
#then it becomes unhashable and cannot be used as a key.
my_dict = {
    (1, 2): "a",
    (3, 4): "b"
}

print(my_dict[(1, 2)])  # Output: a

# 25.What are generator expressions, and why are they often referred to as “tuple comprehensions”?
'''Generator expressions are a concise way to create generators in Python — special iterators 
that yield items one at a time instead of creating the entire list in memory.
They look similar to list comprehensions but use parentheses () instead of square brackets [].'''

#Why are they sometimes called “tuple comprehensions”?
#1.This is a common misconception:
#2.They're not actually tuple comprehensions.
#3.The confusion comes from the use of parentheses, which makes them look like tuples.
#But they return a generator object, not a tuple.
gen = (x * x for x in range(5))
print(gen)         # Output: <generator object ...>

for val in gen:
    print(val)     # Output: 0, 1, 4, 9, 16 (one at a time)

#============================Advanced Tuple Usage====================================================
# 26.How do you combine or concatenate multiple tuples into a single tuple?
'''You can combine or concatenate multiple tuples into a single tuple using the + operator.'''
t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)

combined = t1 + t2 + t3
print(combined)  # Output: (1, 2, 3, 4, 5, 6)

# 27.How can you use the zip() function with tuples to combine elements from two tuples?
'''You can use the zip() function with tuples to pair 
elements from two (or more) tuples into tuples of corresponding elements.'''

t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')

zipped = zip(t1, t2)
result = tuple(zipped)

print(result)  # Output: ((1, 'a'), (2, 'b'), (3, 'c'))


# 28.What happens when you try to modify an element within a tuple? Provide an example.
'''When you try to modify an element within a tuple, Python raises a TypeError because tuples 
are immutable — meaning their contents cannot be changed after creation.'''


# 29.How would you iterate over the elements of a tuple using a for loop?
'''iterate over the elements of a tuple using a for loop just like you would with a list.'''
my_tuple = (10, 20, 30, 40)

for item in my_tuple:
    print(item)
#output
10
20
30
40

# 30.How can you use the enumerate() function with tuples to get both index and value?
'''You can use the enumerate() function with 
    tuples to get both the index and the value of each element while looping.'''

my_tuple = ('a', 'b', 'c')

for index, value in enumerate(my_tuple):
    print(f"Index {index}: Value {value}")
    #output
    # Index 0: Value a
    # Index 1: Value b
    # Index 2: Value c




