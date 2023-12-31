# Arrays
arr = [1, 2, 3]
print(arr)

# Array as stack
arr.append(4)
print(arr)
arr.pop()
print(arr)

# Insert element to array with O(n) complexity
arr.insert(1, 7)
print(arr)
arr[0] = 9 # this is constant time

# Initialize array of size n with default value of 1
n = 5
arr = [1] * n
print(arr, len(arr))
arr = [1, 2] * n
print(arr, len(arr))

# Indexing negative index in array
arr = [1, 2, 3]
print(arr[-1])
print(arr[-2])

# Subarray
arr = [1, 2, 3, 4]
print(arr[1:3])
print(arr[0:4])

# Unpacking an array
a, b, c = [1, 2, 3]
print(a, b, c)

# Loop through array
nums = [1, 2, 3]
# Using index
for i in range(len(nums)):
    print(nums[i])
# Without index
for n in nums:
    print(n)
# With index and value
for i, n in enumerate(nums):
    print(i, n)
# Loop through multiple array simultaneously
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
# Loop through multiple array simultaneously with index
for i, n1, n2 in zip(range(len(nums1)), nums1, nums2):
    print(i, n1, n2)

# Reversing an array
nums = [1, 2, 3, 4, 6]
nums.reverse()
print(nums)

# Sorting array
arr = [3, 7, 9, 5, 1]
arr.sort()
print(arr)

arr = [3, 7, 9, 5, 1]
arr.sort(reverse=True)
print(arr)

# Sorting array of string
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

# Sorting array with custom order
arr.sort(key= lambda x: len(x), reverse=True)
print(arr)

# List comprehension
arr = [ i for i in range(5) ]
print(arr)

arr = [ (i + i) for i in range(5)]
print(arr)

# 2D array
arr = [ [0] * 4 for i in range(4) ]
print(arr)