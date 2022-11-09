# dictionary
dict = {
    "apple": "red", "orange": "orange"
}
# collection of key value pair
# indexing not possible

# accessing value using key
print(dict["orange"])

# update/add value associate with given key
dict["grape"] = "green"
print(dict)

# dictionary methods
d1 = dict.get("Orange")
print(d1)
d2 = dict.keys()
print(d2)
d3 = dict.values()
print(d3)
dict.update({"banana": "yellow"})
print(dict)
d4 = dict.pop("apple")
print(dict)
print(d4)
dict.clear()
print(dict)

# set
set1 = set()
print(type(set1))

# set methods
set1.add(1)
set1.add(2)
set1.add(2)
set1.add(2)
set1.add(2)
print(set1)

# list to set
l1 = [1, 2, 3, 4, 1, 2, 3]
s2 = set(l1)
print(s2)

# set operations
s3 = set1.intersection(s2)
print(s3)

# another method to create set
s4 = {1, 2, 3, 4, 5, 6}
print(type(s4))
s4.remove(2)
s4.pop()
s4.pop()
s4.pop()
print(s4)
