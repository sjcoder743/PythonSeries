# Chapter 3 List
# lists are mutable in python

student = ["rahul", "Rohit", "Anuj", "Shanker"]
# print("Length of student list is : ", len(student))
# print("Student in 0th index is : ", student[0])
# print("Student in 1th index is : ", student[1])
# print("Student in 2nd index is : ", student[2])
# print("Student in 3rd index is : ", student[3])


# List Slicing
marks = [12, 14, 16, 18, 20, 22, 24, 26]
print(marks)
# print(marks[1:4]) # 14,16,18
# print(marks[:4]) # 12,14,16,18
print(marks[:-1])  # 12,14,16,18,20,22,24

# Lists Methods
print("\nLists methods in python")
list = [2, 1, 3]
# 1 list.append(4)
print("append method.......")
list.append(4)
print(list)

# 2 list.insert(idx, el)
print("insert.......")
list.insert(2, 2)
print(list)

# 3 list.sort()
print("sort......")
list.sort()
print(list)

# 4 list.reverse()
print("reverse")
list.reverse()
print(list)

# 5 list.sort(reverse=True)
print("reverse True.....")
list.sort(reverse=True)
print(list)

# list.remove()
print("remove....")
list.remove(2)
print(list)

# list.pop()
print("pop....")
list.pop()
print(list)
