# A tuple is a collection which is ordered and unchangeable.
# Tuples are unchangeable means cannot add new items into a tuple
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisTuple)
print(thisTuple[1])
print(thisTuple[-1])
print(thisTuple[2:5])
print(thisTuple[-4:-1])
print("====== Change Tuple Values =======")
x = ("apple", "banana", "cherry")  # new tuple
y = list(x)  # convert tuple into list
y[1] = "kiwi"  # new value add into list
x = tuple(y)  # convert back into tuple
print(x)

newTuple = ("AA", "BB", "CC", "DD", "EE")
for singleVal in newTuple:
  print(singleVal)

thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "apple" in thisTuple:
    print("Yes, 'apple' is in the fruits tuple")

tupleLength = len(thisTuple)
print("Length: ", tupleLength)
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print("Added Two Tuples:", tuple3)
