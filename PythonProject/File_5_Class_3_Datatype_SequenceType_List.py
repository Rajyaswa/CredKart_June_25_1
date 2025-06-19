a=[1,2,3,4,5]
print(a)
print(type(a))
List1 = [1, 2, 3, 4, 5]
List2 = ["apple", "banana", "cherry"]
List3 = [True, False, True]
List4 = ["apple", 1, True]
List5 = [1, 2, 3, 4, 5]
List6 = [1, 2, "apple", 4, 5]
List7 = ["apple", 1, True, 2, 3]
List8 = ["apple", "banana", "cherry", "Automation Testing", "Credence is Best", 1, True]
print(List1, "\n", List2, "\n", List3, "\n", List4, "\n", List5, "\n", List6, "\n", List7, "\n", List8)
print("\n 03. Operations with List : ")
print("Contact List1 + List2 : ", List1 + List2)
print("Length of List1 : ", len(List1))
print("Repetition of List1 : ", List1 * 3)
print("Membership : ", "C" in List2)
print("Membership : ", "1" in List1) #--> "1"--> string
print("Membership : ", 1 not in List1)
print("Membership : ", 10 not in List1)
print("Index of value 2 in List1 : ", List1.index(2))
print("Count of value 2 in List1 : ", List1.count(2))
print("Value at Index 2 in List1 : ", List1[2])
print("Negative Index of value 2 in List1 : ", List1[-2])
print("Negative Index of value 2 in List2 : ", List2[-1])
print("Slice of List1 : ", List1[1:4])
print("Slice of List1 : ", List1[-4:-1])
print("Slice of List1 : ", List1[1:])# 1,2,3,4,5
print("Slice of List1 : ", List1[:3])# 0,1,2
print("Slice of List1 : ", List1[:])# whole list
print("Slice of List1 : ", List1[::2]) # 1,3,5 # Stepping
print("Slice of List1 : ", List1[::-1]) # 5,4,3,2,1 #reverse
# print("Reverse of List1 : ", List1.reverse())

List1 = [1, 2, 3, 4, 5]
List1.reverse()
print("Reverse of List1 : ", List1)

print("\n 04. List Methods : ")
List1 = [1, 2, 3, 4, 5]
List1.append(6)
print("Append 6 in List1 : ", List1)

List1.insert(2,2.5)
print("Insert 2.5 at 2nd index in List1 : ", List1)

List1.remove(2.5)
print("Remove 2.5 from List1 : ", List1) # specific value

List1.pop()
print("Pop last value from List1 : ", List1)

List1.pop(1)
print("Pop 2nd value from List1 : ", List1) # specific index

List1.clear()
print("Clear List1 : ", List1)

List1 = [1, 2, 3, 4, 5, 6]
List1.extend([7,8,9,2,3,7,0,100])
print("Extend List1 : ", List1)



List1.sort()
print("Sort List1 : ", List1)


List2 = List1.copy() # shallow copy
print("Copy of List1 : ", List2)

List3 = [8,2,3,4,7]

List4 = List3 # direct Copy
print("List4 : ", List4)


# 05. Convert List to String
print("\n 05. Convert List to String : ")
List1 = [1, 2, 3, 4, 5]
print("List to String : ", str(List1))

List1 = ["apple", "banana", "cherry", 100, 150]
print("List to String : ", str(List1))


# Number to String : str(1)

# 06. Convert String to List
print("\n 06. Convert String to List : ")
s1 = "credence is best"
print("String to List : ", list(s1))

