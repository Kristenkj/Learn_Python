"""
args and kargs

"""


def f1(a, b, c):
    return a + b + c


# f1(1) #Passing one argument alone will cause an error

def f2(a2=1, b2=1, c2=1):  # a default value being provided for the args.. will keep error from happening if only
    # one value is given
    return a2 + b2 + c2


result1 = f2(1)
result = f2(3, 2, 5)  # Keep order of number for best practices
print(result1)
print(result)


#THIS ADDS ONE
def print_argument(*args): #able to use and return any number of arguments
    return args

print_argument(2)
print_argument(3,2,4)

