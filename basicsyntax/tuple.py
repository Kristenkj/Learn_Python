"""
Tuple are like lists but they can't be changed.. immutable
They are defined using parentheses
"""

my_list = [1,3,4]
print(my_list)

print("#*" * 30)
my_list[0] = 2 #shows that lists can be changed
print(my_list)

print("#*" * 30)
my_tuple = (1,3,4,5,6,9,8,3,1,1,1,4,5,2)
print(my_tuple)

print("#*" * 30)
print(my_tuple[1]) #Able to access elements

print("#*" * 30)
print(my_tuple[1:]) #Able to slice

print("#*" * 30)
print(my_tuple.index(3)) #Index finds the position of a element


print("#*" * 30)
print(my_tuple.count(1)) #counts the number of times the item/element appears in the tuple