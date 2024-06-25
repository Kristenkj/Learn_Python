#Break

'''
for -> 1 to 10 -> range(1,11,1), range (1,11)
i = 5 - > break from the loop - kicked out from the loop
'''

#the name counter can be switched out for anything
for counter in range (1,11): #counter starts at 1
    #print(counter)#Prints 1-5 because it is before the break statement
    if counter == 5:
        break #this kicks you out of the loop at 5
    #print(counter) #Inside the loop , prints 1 - 4 because 5 immediately kicks out of the loop
print("outside of the loop")