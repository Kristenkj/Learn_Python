"""
Fibonacci Series

0,1,1,2,3,5,8,13, 21
"""

"""
a = 10
b = 12
a, b = a, a + b
print(a, b)
"""

a, b = 0, 1
while a < 10:
    print(a, end="-")#ends=' ' enables the line to be horizontal instead of vertical
    a, b = b, a + b  # a is assigned to b , b is assigned to a + b
