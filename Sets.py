# A set is a collection which is unordered and unindexed.
# written with curly brackets
thisSet = {"apple", "banana", "cherry"}
print(thisSet)

for x in thisSet:
    print(x)

print("banana" in thisSet)  # True

thisSet.add("orange")  # add single item ion set
print(thisSet)

thisSet.update(["mango", "grapes", "pineapple"])  # add multiple items in set
print(thisSet)
print("Length:", len(thisSet))
print(thisSet)
thisSet.remove("pineapple")  # give error is item not exist
thisSet.discard("pineapple")  # give error is item not exist
print(thisSet)
thisSet.pop()  # remove last item from set
print(thisSet)
thisSet.clear()
print(thisSet)
del thisSet
# print(thisSet)
print("========= Join Two Sets ========")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
