# Hash map is dictionary
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
myMap["cupa"] = None
print(myMap)
print(len(myMap))

myMap["alice"] = 0 # constant time complexity
print(myMap)

print("alice" in myMap) # constant time complexity
myMap.pop("alice")

myMap = { "alice": 1, "bob": 2, "cupa": 3}
print(myMap)
myMap = { i: 2*i for i in range(1, 5) }
print(myMap)

# Loop through map
myMap = { "alice": 1, "bob": 2, "cupa": 3}
for key in myMap:
    print(key, myMap[key])
for value in myMap.values():
    print(value)
for k, v in myMap.items():
    print(k, v)