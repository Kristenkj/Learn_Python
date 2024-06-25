# Define the function - Non-return
def greet():
    print("Hello, how are you")


# Call the function
greet()  # doesn't return anything at all .. it just prints the message

print("*************************")

for i in range(5):
    greet()

print("*************************")

result = greet()
print(result)  # this function doesn't return anything
