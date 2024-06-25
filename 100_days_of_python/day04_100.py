user_likes = input("What is your favorite flower? ")
user_hates = input("What is something that makes your blood boil? ")
user_family = (input("What is the name of your sister? ") +
               ", " + input("What is the name of your brother? ") +
               ", " + input("What is the name of your mother? ") +
               " ," + input("What is the name of your father? "))

user_name = input("What is your name? ")
user_pronoun = input("What is your pronoun? Please enter he, she, or they. ")


print(f"{user_name} ran through a field of Daffodils with {user_pronoun} hands high in the airy breeze. {user_pronoun} "
      f"family were standing beside a stream at the bottom of a hill. "
      f"{user_family} was looking at the wildlife in the distance.")
