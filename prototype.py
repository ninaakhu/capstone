tasks = {}

running = True

while running:
    print("Here is your current to do list: ")
    print(tasks)

    wantNewTask = False
    print("Do you want to enter a new task?")
    newTask = input("Enter yes or no")
    if newTask == "yes":
        wantNewTask = True
    elif newTask == "no":
        wantNewTask = False

    if wantNewTask: 
        taskName = input("Enter a task: ")
        dueDate = input("Due date: ")
        priorityLevel = input("Priority level: ")
        tasks[taskName] = {"due_date": dueDate, "priority": priorityLevel, "status": False}
    else:
        wantToQuit = input("Do you want to quit (yes or no): ")
        if wantToQuit == "yes":
            running = False
        elif wantToQuit == "no":
            running = True
