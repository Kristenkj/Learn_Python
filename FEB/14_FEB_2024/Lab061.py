#Reverse a string

""""
str = "Pramod"
rev_str = " "
for c in str:
    rev_str = c + rev_str

print(rev_str)
"""

def rev_string(str):
    str_reverse = ""
    for s in str:
        str_reverse = s + str_reverse
    return str_reverse

#name = rev_string("Kristen")
#print(name)

original_str = input("Enter the string\n")
original_str = original_str.lower()
str_reverse = rev_string(original_str)
print(str_reverse)

if original_str == str_reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")