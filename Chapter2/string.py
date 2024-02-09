name = "this is string"
print("Type of name is : ", type(name))

# basic operations
# 1 Concationtion
val1 = "shanker"
val2 = "joshi"
print(val1 + " " + val2)

# 2 lenth
print("lenth of val1 : ", len(val1))


# 3 Indexing
str = "Shanker_Joshi"
# print(str[0])
# print(str[1])
# print(str[-3])
# print(str[-2])

# 4 Slicling
# print(str[1:4]) # gives han
# print(str[:4]) #shan
# print(str[1:]) # h to last index

#  slicing with negative index
str = "Apple"
print(str[-3:-1])

# String function
# print("Strings methods....")
# str = "python i am a coder of python now python"
# print(str.endswith("coder"))
# print(str.count("python"))
# print(str.capitalize())
# print(str.replace("python", "PYTHON"))
# print(str.find("coder"))


# WAP to input user’s first name & print its length.
# name = input("Enter your first name : ")
# print(name + ", Lenth = ", len(name))


# WAP to find the occurrence of ‘$’ in a String.
str = "A$ppl$e"
print(str.count("$"))
