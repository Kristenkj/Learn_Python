"""
and
**************************
True and True --> True
True and False --> False
False and False --> False

or
**************************
True or True --> True
True or False --> True
False or False --> False

not
**************************
Not True --> False
Not False --> True
"""

and_output1 = (10 == 10) and (9 <= 11)
print(and_output1)
print("*#" * 30)


and_output2 = (19 >= 30) and (9 == 11)
print(and_output2)
print("*#" * 30)

and_output3 = (10 != 10) and (9 >= 11)
print(and_output3)
print("*#" * 30)

the_or_output1 = (10 == 10) or (9 <= 11)
print(the_or_output1)
print("*#" * 30)

the_or_output2 = (10 == 10) or (9 >= 11)
print(the_or_output2)
print("*#" * 30)

the_or_output3 = (11 == 10) or (9 == 11)
print(the_or_output3)
print("*#" * 30)

not_output1 = not (10 == 10)
print(not_output1)
print("*#" * 30)

not_output2 = not (9 >= 11)
print(not_output2)
print("*#" * 30)

"""
Order of precedence:
1. not
2. and
3. or

Anything in parentheses will be evaluated first.
Expressions are evaluated from left to right
"""

bool1_output = True or not False and False
print(bool1_output)
print("*#" * 30)

bool2_output = 10 == 10 or not 2 < 2 and 3 >= 3
print(bool2_output)
print("*#" * 30)

bool3_output = (10 == 10 or not 2 < 1) and 3 > 3
print(bool3_output)
print("*#" * 30)