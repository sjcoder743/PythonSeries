# tupples are immutable in python
tup = (12, 13, 14, 15, 16, 17, 18, 19, 20, 16)
print(tup)

print(tup.index(16))
# returns index of first occurrence


el = 16
print(tup.count(el))


# Practice Question

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
"""mov1 = input("Enter your favourite movie : ")
mov2 = input("Enter your favourite movie : ")
mov3 = input("Enter your favourite movie : ")

listOfMuvie = [mov1, mov2, mov3]
print("List of movies are : ", listOfMuvie)"""

# WAP to check if a list contains a palindrome of elements.
list = [1, 2, 3, 2, 1]
print(list)
copiedList = list.reverse.copy()
if copiedList == list:
    print("Palindrome")
else:
    print("Not palindrome")
