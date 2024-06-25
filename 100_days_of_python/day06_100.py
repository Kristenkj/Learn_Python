user_name = input("What is your name? ")

print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if (username == "mark" or username == "suzzy" or
    username == "kristen") and password == "password":
  print("Welcome ", user_name, " you are now logged in!")
else:
  print("You are not registered in out system! Please create an account.")