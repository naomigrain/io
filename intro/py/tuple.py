# Tuple is immutable array
# Can be used as key for hash map/set
tuple = (1, 2)
print(tuple[0])

mySet = set()
mySet.add(tuple)
print((1, 2) in mySet)
print((2, 1) in mySet)

myMap = { (1, 2): 3 }
print(myMap[(1, 2)])