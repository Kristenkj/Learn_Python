"""
Continue
"""

for num in range(1, 10):
    print(num)

print("************************")

for num in range(1, 10):
    if (num > 1):
        print(num)

print("************************")

for num in range(1, 10):
    if num % 2 == 0:
        print(num)

print("************************")

for num in range(1, 10):
    if num % 2 == 0:
        print(f"Found Even number {num}")

print("************************")

for num in range(1, 10):
    if num % 2 == 0:
        print(f"This is a Even number {num}")
    else:
        print(f"This is a ODD number {num}")

# How to use continue

print("*************************")

for num in range(1, 10):
    if num % 2 == 0:
        print(f"This is a Even number {num}")
        continue
    print(f"This is a ODD number {num}")  # This code will only be run when the if loop is not running

