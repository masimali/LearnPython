thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisDict)

x = thisDict["model"]
print(x)
y = thisDict.get("model")
print(y)

thisDict["year"] = 2018
print(thisDict)

for i in thisDict:
    print(i)  # get key names
    print(thisDict[i])  # get all values

for x in thisDict.values():  # values of a dictionary
    print(x)

for x, y in thisDict.items():  # both keys and values
    print(x, y)

if "model" in thisDict:
    print("Yes, 'model' is one of the keys in the thisDict dictionary")
print("Length: ", len(thisDict))

thisDict["color"] = "red"  # Add item in dictionary
print(thisDict)

myDict = thisDict.copy()
print(myDict)

thisDict.pop("model")  # removes the item with the specified key name
print(thisDict)

thisDict.popitem()  # removes the last inserted item
print(thisDict)

del thisDict["year"]  # removes the item with the specified key name
print(thisDict)

thisDict.clear()  # empties the dictionary
print(thisDict)

del thisDict  # delete the dictionary completely
# print(thisDict)

child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
print(myfamily)
