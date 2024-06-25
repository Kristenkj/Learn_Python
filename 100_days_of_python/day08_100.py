name = input("What is your name? ")
week_day = input("What day of the week is it? ")
goal_1 = input("What is your first goal for the quarter? ")
goal_2 = input("What is your second goal for the quarter? ")

if week_day.capitalize() == "Monday":
    print(f"Say this affirmation out loud: I {name} will have an amazing week. Nothing will stand in my way.")
elif week_day.capitalize() == "Tuesday":
    print(f"Say this affirmation out loud: I {name} am one step closer to completing my first goal of the quarter to {goal_1}")
elif week_day.capitalize() == "Wednesday":
    print("Say this affirmation out loud: I am becoming more successful everyday")
elif week_day.capitalize() == "Thursday":
    print("Repeat this affirmation: Everything is working out for my good")
elif week_day.capitalize() == "Friday":
    print(f"I {name} have the knowledge and strength to complete my goal to {goal_2}")

print(f"Your are amazing {name}! Have a wonderful day!")