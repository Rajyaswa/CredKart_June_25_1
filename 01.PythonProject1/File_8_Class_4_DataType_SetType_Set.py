a={2,7,12,15,17}
print(a)
print("data type of a is =",type(a))
Set1 = {1, 2, 3, 4, 5, 5,6,7,7,7,7}
Set2 = {"apple", "banana", "cherry"}
Set3 = {True, False, True}
Set4 = {"apple", "banana", "cherry", "Automation Testing", "Credence is Best", 1, True}

print(Set1)
print(Set2)
print(Set3)
print(Set4)
Set4.add(7)
print(Set4)
Set4.remove(True)
Set3.discard(7)
Set2.clear()
print(Set2)

set1={2,4,6,8,10,12,14,16,18}
set2={3,9,12,15,18,21,24}

print(set1.difference(set2))
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
Set1 = {1, 2, 3, 4, 5}
Set2 = {4, 5, 6, 7, 8}
Set3 = {9,10,11}
Set4 = {9,10,11}
Set5 = {1,2,3,4,5,6,7,8,9,10,11}

print( Set1.isdisjoint(Set2))
print(Set1.isdisjoint(Set3))
print( Set1.issubset(Set2))
print(Set4.issubset(Set5))
print(Set1.issuperset(Set2))
print( Set3.issuperset(Set4))
print(Set3.issubset(Set4))
a = frozenset({1, 2, 3, 4, 5})
print(a)
print("The data type of a is", type(a))
print("\n07. Convert Set to List : ")
Set1 = {1, 2, 3, 4, 5}
List1 = list(Set1)
print("Convert Set to List : ", List1)


print("\n08. Convert Tuple to Set : ")
Tuple1 = (1, 2, 3, 4, 5)
Set1 = set(Tuple1)
print("Convert Tuple to Set : ", Set1)
