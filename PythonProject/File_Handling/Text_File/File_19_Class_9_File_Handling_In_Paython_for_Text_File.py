print("Example:1 Text file read")
file=open(r"C:\Users\SMAK\PycharmProjects\PythonProject1\File_Handling\Text_File\File1.txt","r")
print(file.read())
file.close()


print("Example2:Text file write")
file=open(r"C:\Users\SMAK\PycharmProjects\PythonProject1\File_Handling\Text_File\File1.txt","w")
file.write("where r u")
file.close()

print("Example:write new text file")
file=open(r"C:\Users\SMAK\PycharmProjects\PythonProject1\File_Handling\Text_File\File2.txt","w")
file.write("hi swaroop")
file.close()


print("Example:append file")
file=open(r"C:\Users\SMAK\PycharmProjects\PythonProject1\File_Handling\Text_File\File2.txt","a")
file.write("hi swaroop")
file.close()

print("\nExample 6 Program to generate multiplication table")
for i in range(2,11): # 2 to 10
    file_name = "Table_Of_" + str(i) + ".txt"
    file = open(r"C:\Users\SMAK\PycharmProjects\PythonProject1\File_Handling\Text_File\File2.txt" + file_name,"w")
    for j in range (1,11): # 1 to 10
        file.write(str(i) + " * " + str(j) + " = " + str(i*j) + "\n")
    file.close()