"""
Examples to show how strings work in python

Sequence of characters
Contains a-z, 0-9, @


Can use double or single quotes
    *Note: quotes have to stay consistent for a word or phrase
        Not allowed: "Hello World'

"""
a = "This is a simple string"
b = 'Using single quotes'

print("********************************************************************************************")

print(a)
print(b)

print("********************************************************************************************")

c = "Need to use 'quotes' inside a string"
d = 'Need to use "quotes" inside a string'
# Can't use double quotes inside "" but able to mix-match the single and double if wanting to emphasize something
print(c + " " + d)

print("********************************************************************************************")

# Backslash (\) will ignore the double quote
e = "Another way to handle \"quotes\""
print(e)

print("********************************************************************************************")

# \n will split the string
y = "Hellow out there over the\n moon is red and blue"
print(y)

print("********************************************************************************************")
"""
Now we will go over string methods in Python
"""
# Accessing characters in a string
# Index starts from zero in Python - n is on the zero index, y is on the first index, c is on the second index
first_index = "nyc"[1]
second_index = "nyc"[2]
print(first_index)
print(second_index)

"""
len() - Space is counted as a character
lower()
upper()
str()
"""

strip = "This is a mixed case"
print(strip.lower())
print(strip.upper())
print(len(strip))
print(strip + " " + str(2))

"""
Concatenation of string is done with the (+ " " +)
Can only add strings to each other. Not able to mix data types without conversion
"""
#Replace Method
# How to replace something (maybe a pattern) within a string
a = "abcdefghijklmnopqrstuvwxyz"
print(a.replace("abc", "ABC", 1))

b = "1abc2abc3abc4abc5abc"
print(b.replace("abc", "HGW", ))

c = "1abc2abc3abc4abc5abc"
print(c.replace("abc","ABC", 3))

#Sub-strings
sub = a[1]
print(sub)

print("***********************************************************************")

sub = b[1:6]
print(sub)
#The starting index is inclusive and the ending is exclusive

print("***********************************************************************")

sub = b[1:6:2]
print(sub)
#The last number causes skips: If 2 is the last number there is one skip. If 3 is the last number there are two skips

print("***********************************************************************")

sub = a[:]
print(sub)
#Everything is shown - complete string because there is no starting index and no ending index

print("***********************************************************************")

sub = a[1:]
print(sub)
#Starts from the first and goes to the last - Remember the first index (the first index is the one that is indicated.. It's not necessarily 1) is inclusive

print("***********************************************************************")

sub = a[:7]
print(sub)
#Everything is included up until 7 (which is not included)

print("***********************************************************************")

sub = a[-6]
print(sub)
#starts at the end of the string

print("***********************************************************************")

sub = a[:-6]
print(sub)
#Trims off at the end if negative

print("***********************************************************************")

sub = a[::-6]
print(sub)
#Reverses string with the :: in front of the numbers

"""
How to format strings in python
"""
city = "nyc"
event = "show"

print("Welcome to" + " " + city + " " + "and enjoy the" + " " + event)
print("Welcome to %s"% city)
print("Welcome to %s and enjoy the %s"% (city, event))
# %s is a placeholder for the variables - cleans code: variables you want to use are provided at the end

print('Hello Kristen')