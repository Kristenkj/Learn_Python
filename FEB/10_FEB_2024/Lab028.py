#Condition
#age > 18 -> You are allowed to go out
#age < 18 -> You are not allowed to go out

age = int(input("Enter your age"))
# if condition: -> return true or false
if age > 18:
    print("You are allowed to go out")
else:
    print("You are not allowed to go out")

a = 8

if a == 5:
    print("Hi")
else:
    print("Bye")

x = 20
y = 10

# x > y ->
# y > x ->
# x== y


if x > y:
    print("X > y")
elif x < y:
    print("x < y")
else:
    print("X and Y are equal")