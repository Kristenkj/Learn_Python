"""
Assignment Operator
*Stores the value of the variable literal to the identifier

Unary Operator
*Single value or literal

Not Operator - Unary
*Applied to booleans only

is Operator
*Checks for identity
"""

name = 'Kristen' #Assignment
my_bank_balance = -100 #Unary
age = 35 #Unary
is_Married = True

a = 5
b = 5
c = 6
print(a is b)#True
print(a is c)#False

my_list = [1,2,3]
my_list2 = [1,2,3]
print(my_list2 is my_list)#False


print(age)
print(my_bank_balance)
print(not(is_Married))#Not operator