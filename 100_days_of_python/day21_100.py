number_to_multiply = int(input("Enter a number that you want the multiples of: "))

count = 0

for i in range (0, 11, 1):
  answer_guess = int(input(f"What do you think {number_to_multiply} * {i} the answer is? "))
  answer_guess_1  = i, "*",number_to_multiply,"=", answer_guess
  correct_answer = i * number_to_multiply
  if answer_guess == correct_answer:
    count += 1
    print("Correct! ", answer_guess_1)
    continue
  elif answer_guess_1 != correct_answer:
    print("Incorrect! The correct answer is ", i * number_to_multiply)
    #print("You scored", i, "out of 10")
    break
  else:
    break

if count == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You got", count, "out of 10 correct.")