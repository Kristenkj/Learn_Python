print("To-do list manager")
print()

todoList = []

def todoListManager():
  for item in todoList:
    print(item)

while True:
  menu = input("Do you want to view, add, or edit your to-do list?")
  if menu == "add":
    item = todoList.append(input("What do you want to add to your to-do list?"))
  elif menu == "edit":
    item = input("What do you want to remove from your to-do list?")
    if item in todoList:
      todoList.remove(item)
    else:
      print(f"{item} was not in the list")
  elif menu == "view":
    print(todoList)
  else:
    print("Invalid input")
    continue
  todoListManager()