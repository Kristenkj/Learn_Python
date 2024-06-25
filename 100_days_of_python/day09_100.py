generation_identifier = int(input("What year were you born in? "))

if generation_identifier >= 1925 and generation_identifier <= 1946:
    print("You are considered to be a part of the Traditionalists")
elif generation_identifier >=1947 and generation_identifier <= 1964:
    print("You are considered to be apart of the Baby Boomers")
elif generation_identifier >= 1965 and generation_identifier <= 1981:
    print("You are considered to be a part of Generation X")
elif generation_identifier >= 1982 and generation_identifier <= 1995:
    print("You are considered to be a part of the Millenials")
elif generation_identifier >= 1996 and generation_identifier <= 2015:
    print(" You are considered to be a part of Generation Z")
else:
    print("Your generation hasn't been classified yet. You are considered an alien until further notice.")