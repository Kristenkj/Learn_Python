myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent?"))
total_amount = round(((answer * (tip/100)) + answer), 2)
print("You all owe", total_amount)
