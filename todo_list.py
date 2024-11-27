tasks = []

while True:
    action = input("Add/View/Quit: ").lower()
    if action == "add":
        task = input("Enter a task: ")
        tasks.append(task)
    elif action == "view":
        print("To-Do List:", tasks)
    elif action == "quit":
        break
    else:
        print("Invalid choice!")