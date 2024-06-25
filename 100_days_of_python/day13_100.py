test_name = input("What is the name of the test? ")
print()
max_score = int(input("What is the maximum score? "))
points_received = int(input("How many points did you receive? "))

number_score = float(points_received / max_score)
final_number = round(number_score, 2)
point_percentage = round(float(points_received / max_score)*100, 2)


if point_percentage >= 90 and point_percentage <= 100:
  print("Your letter grade is an A+")
elif point_percentage >= 80 and point_percentage <= 89:
  print("Your letter grade is an A")
elif point_percentage >= 70 and point_percentage <= 79:
  print("Your letter grade is a B")
elif point_percentage >= 60 and point_percentage <= 69:
  print("Your letter grade is a C")
elif point_percentage >= 50 and point_percentage <= 59:
  print("Your letter grade is a D")
elif point_percentage < 50:
  print("Your letter grade is a U")