"""
Data type to store more than one value in one variable name, in terms of key value pair
Dictionary items are in brackets {} in key:value pairs, separated with ", "
exp of a dictionary: {'k1':'v1','k2':'v2'}
Not sequenced, no indexing... just mapping (Can appear in any order)
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
print(car)
d = {}  # defining empty dictionary
model = car['model']

print(car['make'])  # unable to run print:(car[0]) because dictionaries aren't indexed
print(model)

d['one'] = 1  # adding more items to a dictionary
d['two'] = 2
print(d)

sum_1 = d['two'] + 8
sum_3 = d['two'] = sum_1 + 12
print(sum_1)
print(sum_3)


"""
Nested dictionaries
d = {'k1':{'nestk1':'nestvalue1', 'nestk2':'nestvalue2'}}
d['k1']['nestk1']
"""

cars = {'BMW': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}
bmw_year = cars['BMW']['year']
print(bmw_year)
print(cars['benz']['model'])

print("#*" * 20)
print(car.keys())
print(cars.keys())
print("#*" * 20)
print(car.values())
print(cars.values())

print("#*" * 20)
#To see keys and values together use items
print(car.items())
print(cars.items())

print("#*" * 20)
car_copy = car.copy() #creates a copy of the dictionary
print(car_copy)

print("#*" * 20)
#car.clear() #This code clears the dictionary
#print(car)

print(car.pop('model')) #this pops out a value/key from the dictionary...
# It will no longer be included in the dictionary
print(car)