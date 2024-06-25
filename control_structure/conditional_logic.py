"""
Conditional logic
"""

if 100 > 20:
    print("Hundred is greater than twenty")

print("#*" * 30)

color1 = "brown"

if color1 == "green":
    print("GO!")
elif color1 == "yellow":
    print("Slow down")
elif color1 == "red":
    print("STOP!")
else:
    print("Error in console. Contact your local IT department.")


print("#*" * 30)

"""
While Loops
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are strings, lists, tuples and dictionaries

"""
x = 0
while x < 8:
    print("Value of x is:  " + str(x))
    x = x + 1

l = []
num = 0
while num < 10:
    l.append(num)
    print("Value of num is: " + str(num))
    num += 1

print(l)

"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""

"""

p = 0
while p < 8:
    print("Value of p is:  " + str(p))
    p = p + 1

    if p == 8:
        break
        print("This example is awesome")
        print("#*" * 20)
        
"""
m = 0
while m < 15:
    print("Value of m is:  " + str(m))
    m = m + 1

    if m == 8:
        continue
    print("This example is awesome")
    print("#*" * 20)

r = 0
while r < 8:
    print("Value of r is:  " + str(r))
    r = r + 1

    if r == 8:
        break
        print("This example is awesome")
        print("#*" * 20)
else:
    print("Just broke out the loop")
    # else will not execute if the break statement runs

print('$' * 30)
"""
For Loop
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are strings, lists, tuples and dictionaries    
"""
# Prints the string going down
my_string = 'abcabc'

for c in my_string:
    print(c)

print('*#' * 20)

# Prints the string going across
my_string = 'abcabc'

for c in my_string:
    print(c, end=' ')

# print('*#' * 5)


# Replaces the little a with a BIG A
my_string1 = 'abhabh'

for c in my_string1:
    if c == 'k':
        print('A', end=' ')
    elif c == 'p':
        print(c, end=' ')
    else:
        print("Invalid")


print('*#'*20)
print('Hello World')