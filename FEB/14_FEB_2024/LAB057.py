"""
Functions - Blocks of code - which can be executed
They can return something
They can't return something - non-return

They have parameters
They don't have parameters/arguments
"""


# Define by using def:
# Non-return type and no parameter/argument
def say_hello():  # say_hello is the name of the function
    # Write the code
    print("Hello")


# Call the function

say_hello()  # prints Hello


# Return Type
def say_hello_arg(name):
    print("Hello", name)


say_hello_arg("Kristen")


def say_hello_args(name="Demo Name", age=0):
    print("Hello", name, ". ", f"You are {age} years old.")


say_hello_args("Kristen", 28)
say_hello_args()  # if nothing is entered then the default values will result

def sum_number_argument_ret (a,b):
    return a+b

result = sum_number_argument_ret(2,4)
print(result)
