# To insert value in constant time
# And to search value in constant time
mySet = set()

mySet.add(1) # constant
mySet.add(2) # constant
print(mySet)

print(len(mySet))
print(1 in mySet) # constant time
print(2 in mySet) # constant time
print(3 in mySet) # constant time

mySet.remove(2) # constant time
print(2 in mySet) # confirm if it's has been removed/not

# List to set
print(set([1, 2, 3, 4, 3]))

# Set comprehension
mySet = { i for i in range(5) }
print(mySet)