question_1 = input("Are you a fan of the show 'The Chilling Adventures of Sabrina'? ")
if question_1.lower() == "yes":
    print("Great! Let's see if you're a real fan.")

    question_2 = input("Who is the main character? ")
    if question_2.capitalize() == "Sabrina":
        print("Correct!")
        question_3 = input("What is the name of Sabrina's best friend? ")
        if question_3.capitalize() == "Roz":
            print("Correct!")
            question_4 = input("What is the name of Sabrina's mother? ")
            if question_4.capitalize() == "Diana":
                print("Correct!")
            else:
                print("Incorrect. The correct answer is Diana.Go watch the show again.")
        else:
            print(f"Incorrect. The correct answer is Roz. You answered {question_3}.")
            question_4 = input("What is the name of Sabrina's mother? ")
            if question_4.capitalize() == "Diana":
                print("Correct!")
            else:
                print("Incorrect. The correct answer is Diana.Go watch the show again.")
    else:
        print(f"Wrong! The correct answer is Sabrina. You said {question_2}.")
        question_3 = input("What is the name of Sabrina's best friend? ")
        if question_3.capitalize() == "Roz":
            print("Correct!")
            question_4 = input("What is the name of Sabrina's mother? ")
            if question_4.capitalize() == "Diana":
                print("Correct!")
            else:
                print("Incorrect. The correct answer is Diana.Go watch the show again.")
        else:
            print(f"Incorrect. The correct answer is Roz. You answered {question_3}.")
            question_4 = input("What is the name of Sabrina's mother? ")
            if question_4.capitalize() == "Diana":
                print("Correct!")
            else:
                print("Incorrect. The correct answer is Diana.Go watch the show again.")

elif question_1.lower() == "not sure":
    print("Well, you should watch it!")
elif question_1.lower() == "no":
    print("You should watch it!")
else:
    print("Go watch the show! It is epic!")