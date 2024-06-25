"""
Pass - > Skip the code
"""
#Prints 0 - 9
for i in range (10):
    print(i)

print("***************************")

#Prints values 0-9 but skips 5
for i in range (10):
    if i == 5:
        pass
    else:
        print(i)

print("***************************")

#Prints values 0 - 4 because the print statement is after the break statement.
# The break statement makes the code stop; which is why it doesn't go any further.
for i in range (10):
    if i == 5:
        break
    else:
        print(i)