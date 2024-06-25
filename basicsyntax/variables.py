
"""
table
object reference count
"""

city = 'NYC'
city1 = 'NYC'
population = 34


print(city + " " )
print(population)

population = 123
city = 'GA'
#The value of city changed to GA

print(city + " " + city1)
print(population)

"""
Now we are going over booleans
Always either True (1) or False (0)
zero in any form is False
Nul/None = False
"""

a = True
b = False

print(a)
print(b)

print("********************************")

print(bool(0))
print(bool(1))
print(bool(3))

c = ""
print(bool(c))

h= ("Some value")
print(bool(h))