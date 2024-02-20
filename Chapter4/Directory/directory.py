dict = {
    # "key" : "value" like object in javaScript
    "name": "Shanker",
    "marks": "99",
    "cgpa": 9.6,
    "subjects": ["physics", "cs", "math"],
}
# print(dict)
# print("printing specific value with the help of key: ", dict["name"])
# for indivisual print
""" 
print(dict["marks"])
print(dict["subjects"])
print(dict["cgpa"])
"""

# nested directory
nestedDict = {
    "name": "sjoshi",
    "age": 14,
    "sports": {"cricket": 3, "basketball": 5, "racket": 2},
}
# print(nestedDict)
# print("printing specific key : ", nestedDict["sports"])
# print(
#     "printing specific nested value with the help of key: ",
#     nestedDict["sports"]["basketball"],
# )


"""  
directory methods
1 .keys()
2 .values()
3 .items()
4 .get()
5 .update()
"""

# print(nestedDict.keys())
# print(nestedDict.values())
# print(nestedDict.items())
nestedDict.update(dict)
print(nestedDict)


# Creating a dictionary
myDict = {"key": "value", "another_key": "another_value"}
result = myDict.get("key")
print(result)

