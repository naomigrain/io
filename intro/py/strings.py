# Strings can be indexed
s = "abc"
print(s[0:2])

# We can't modify a string by indexing it
# s = "abc"
# s[0] = "z"
# print(s)

# We can't modify the string by this instead
s = "abc"
s += "def"  
# But instead directly modify the string
# we create new string
# So the time complexity is O(n)
print(s)

# String can be converted to int and float
print(int("123") + int("124"))
print(float("1.5") * int("6"))
# But all character should be numerical
# print(int("12a12")) # We can't do this

# Numbers also can be converted to string
print(str(123) + str(124)) # 123124

# Get the ascii values
print(ord("a"))
print(ord("B"))

# Joining string with delimiter
strings = ["ab", "bc", "cd", "de", "ef"]
print("".join(strings))
print(",".join(strings))
print(":".join(strings))