students = ["kaisamba", "Foday", "Sharon"]

print(students)

print (f"My best friend is {students[0]}")
print (f"My best friend is {students[1]}")
print (f"My best friend is {students[2]}")

# Get the index of an item in alist 
print(students.index("kaisamba"))
print(students.index("Sharon"))

#Know the number of items in a list 
print(len(students))

#How we add items to a list 
students.append("Isatu")
print(students)

students += {"Kadiatu", "John", "Bintu"}
print(students)


students.insert(4,"Khadija")
print(students)

#Extending a List 
fruits = {"Apple", "Banana", "Mango"}
studnets.extend(fruits)
print(students)

#removing an item from a list
fruits.remove("Mango")
print(fruits)

students.pop()
students.pop()
thirdItem = students.pop()
print(students)
print(thirdItem)