set1 = {1, 2, 3, 4}
set2 = {11, 22, 33, 44}
print("Before add element in set: ", set1)
# Add method
set1.add(5)
print("After add element in set: ", set1)

print("Before add element in set: ", set2)
set2.add(55)
print("After add element in set: ", set2)

#  Remove method
removeSet = {1, 2, 3, 4}
print("Before remove the element with the set: ", removeSet)
removeSet.remove(2)
print("After remove the element with the set: ", removeSet)

# clear method
setToBeClear = {11, 22, 33, 44, 55}
setToBeClear.clear()
print(setToBeClear)

# pop method (remove random  element from the set)
randomRemove = {1, 23, 36, 7, 6, 78}
print("Before remove : ", randomRemove)

randomRemove.pop()
print("After remove : ", randomRemove)


#  union and intersection method
unionSet = set1.union(set2)
print(unionSet)

interSectionSet = set1.intersection(removeSet)
print(interSectionSet)
