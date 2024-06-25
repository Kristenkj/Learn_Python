scale = int(input("Enter your grade to find your letter grade"))

if scale > 90 and scale < 100:
    print("Your letter grade is A")
elif scale > 80 and scale < 89:
    print("Your letter grade is B")
elif scale > 70 and scale < 79:
    print("Your letter grade is C")
elif scale >= 60 and scale <= 69:
    print("Your letter grade is D")
elif scale >= 0 and scale <= 59:
    print("Your letter grade is F")
else:
    print("Error: Please choose a number between 0 and 100")
