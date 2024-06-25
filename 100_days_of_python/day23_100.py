def userLogin():
  while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "admin":
      print("Login successful!")
      break
    else:
      print("Incorrect username or password.")
      continue

print("Welcome to the login system!")
userLogin()
