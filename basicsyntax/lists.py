"""
Data type to store more than one value in one variable name
List items are in brackets, separated with " , " [1,3,4]
"""

cars = ["BMW", "Honda", "AUDI", "Acura", "Subaru"]
empty_list = []
print(cars)
print(empty_list)

print("*#" * 20)

print(cars[0])

num_list = [1, 2, 3]
sum_num = num_list[0] + num_list[1]
print(sum_num)

more_cars = ["BMW", "Honda", "AUDI"]
print(more_cars[1])

more_cars[1] = "Benz"
print(more_cars[1])
print(more_cars)

length = len(cars)
print(length)

# Adding more items into the list with append at the end of the list

cars.append("Benz")
print(cars)

# Adding more items into the list but at the preferred index with insert

cars.insert(1, "Jeep")
print(cars)

# Finds the index of any item of the list. If there are two duplicate items in the list ...
# It will give the 1st instance of that item in the index
x = cars.index("Honda")
print(x)

# How to remove last item from a list
y = cars.pop()
print(y)
print(cars)

# How to remove a particular item from the list
cars.remove("Jeep")
print(cars)

# How to slice items from a list:
# The '0' is inclusive but the '2' isn't. So,it will not be included.
slicing = cars[0:2]
print(slicing)
print("#*" * 20)
slicing1 = cars[1:3]
a = cars[1:]
print(slicing1)
print("#*" * 20)
print(a)
print("#*" * 20)
print(cars)
print("#*" * 20)

#This sorts the list
#AUDI is listed before Acura because all the letters are capitalized
cars.sort()
print(cars)