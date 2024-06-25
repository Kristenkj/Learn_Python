def make_pizza(*toppings):
    # for toppings in toppings: #Can use for loop
    # print(toppings)
    print(toppings)  # Can use tuple


Kristen = make_pizza("beef", "cheese", "pineapple")
Hunter = make_pizza("Mushroom", "Avocado", "Onion")


def make_pizza_base(*toppings, base ="Thick Crust"):#The star means multiple * [Only one parameter can be multiple]
    print(toppings, base)
    #for topping in toppings:
        #print(topping)


Riley = make_pizza_base("cheese", "beef", base="thin")
Avery = make_pizza_base("cheese", "beef", )
