# Nested function have access to outer variables
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    
    return inner()

print(outer("a", "b"))

# Nested function can modify objects but not reassign
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # will only modify val in the helper scope
        # val *= 100

        # this will modify val outside helper scope
        nonlocal val
        val *= 2

        return arr, val
    
    return helper()

print(double([1, 2, 3], 9))
        