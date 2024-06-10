import tkinter as tk # imports library
from tkinter import messagebox

root = tk.Tk() # window called root
root.configure(bg="white") # background is white

def add_task():
    taskName = taskEntry.get()
    dueDate = dueDateEntry.get()
    priorityLevel = priorityEntry.get()

    if taskName.strip():
        tasks[taskName] = {"due_date": dueDate, "priority": priorityLevel, "status": False}
        update_listbox()
        taskEntry.delete(0, tk.END)
        dueDateEntry.delete(0, tk.END)
        priorityEntry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task name cannot be empty.")

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task_name, task_details in tasks.items():
        task_str = f"Task: {task_name}, Due Date: {task_details['due_date']}, Priority: {task_details['priority']}"
        listbox_tasks.insert(tk.END, task_str)

root.geometry("800x500") # dimensions of window x=800, y=500
root.title("To Do") # window title is To Do

titleLabel = tk.Label(root, text="To Do List", font=('Arial', 18)) # creating the title as a label, it's a part of window 'root'
titleLabel.pack(padx=20, pady=20) # packs the label onto the window

# entry is a textbox with height 1, no multi-line feature
taskEntry = tk.Entry(root, width=40) 
taskEntry.pack(pady=5)

dueDateEntry = tk.Entry(root, width=40)
dueDateEntry.pack(pady=5)

priorityEntry = tk.Entry(root, width=40)
priorityEntry.pack(pady=5)

addTask = tk.Button(root, text="Add Task", command=add_task)
addTask.pack(pady=5)

listbox_tasks = tk.Listbox(root, height=15, width=40)
listbox_tasks.pack()

tasks = {}

root.mainloop() # creates a window

tasks = {}

# running = True
running = False

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

# deleting a task, editing a task, completing
# creating a new to do list interface
# sub tasks

# running = False

# print("Task name: "+user_input+", Due date: "+user_input2+", Priority level: "+user_input3)

# tasks["task1"] = {"due_date": "2023-06-10", "priority": 1, "status": False}
# tasks["task2"] = {"due_date": "2023-06-11", "priority": 2}