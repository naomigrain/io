import math

"""
    Division
"""
# By default, python uses decimal division, while most
# language using integer division
print(5 / 2)
print(5 // 2) # bulatkan kebawah
# CAREFUL : most language round towards 0 by default
# so negative numbers will round down
print("CAREFUL", -3 / 2)
print("CAREFUL", -3 // 2)
print("SOLUTION", int(-3 / 2))

"""
    Modulo
"""
print(10 % 3)
print("CAREFUL", -10 % 3) # result will be 2
print(math.fmod(-10, 3))

"""
    Math helpers
"""
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(16)) # returns float
print(math.pow(2, 3)) # returns float

"""
    Min/max value
"""
print(float("inf"))
print(float("-inf"))
print(math.pow(2, 200) < float("inf"))