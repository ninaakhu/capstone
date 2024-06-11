import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import datetime
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        root.configure(bg="#F2CBFF")

        # Set default font
        default_font = ("Courier New", 10)

        # Task entry frame
        self.frame = tk.Frame(root, bg="#F2CBFF")
        self.frame.pack(pady=10)

        # Task name
        self.task_label = tk.Label(self.frame, text="Task Name:", font=default_font)
        self.task_label.grid(row=0, column=0, padx=5, sticky="w")

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=40, font=default_font)
        self.task_entry.grid(row=1, column=0, padx=5)

        # Due date
        self.date_label = tk.Label(self.frame, text="Due Date:", font=default_font)
        self.date_label.grid(row=0, column=1, padx=5, sticky="w")

        self.date_entry = DateEntry(self.frame, width=12, background='darkblue',
                                    foreground='white', borderwidth=2, year=datetime.datetime.now().year, font=default_font)
        self.date_entry.grid(row=1, column=1, padx=5)
        self.date_entry.bind('<KeyPress>', lambda e: "break")  # Disable typing

        # Priority
        self.priority_label = tk.Label(self.frame, text="Priority:", font=default_font)
        self.priority_label.grid(row=0, column=2, padx=5, sticky="w")

        self.priority_var = tk.StringVar(value="3")
        self.priority_dropdown = ttk.Combobox(self.frame, textvariable=self.priority_var, values=("1", "2", "3"), width=5, state="readonly", font=default_font)
        self.priority_dropdown.grid(row=1, column=2, padx=5)

        # Add button
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task, font=default_font)
        self.add_button.grid(row=1, column=3, padx=5)

        # Create a canvas for the task list and add a scrollbar
        self.canvas = tk.Canvas(root, bg="#F2CBFF")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.task_list_frame = tk.Frame(self.canvas, bg="#F2CBFF", width=100)
        self.canvas.create_window((0, 0), window=self.task_list_frame, anchor="nw")

        self.tasks = []

        # Update the scrollregion of the canvas whenever the task list frame changes size
        self.task_list_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def add_task(self):
        task_name = self.task_var.get()
        due_date = self.date_entry.get_date()
        priority = self.priority_var.get()

        if task_name:
            task = {"name": task_name, "due_date": due_date, "priority": int(priority)}
            self.tasks.append(task)
            self.display_tasks()

            self.task_var.set("")
        else: 
            messagebox.showwarning("Warning", "Task name cannot be empty.")

    def display_tasks(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        # Sort tasks by priority before displaying them
        self.tasks.sort(key=lambda task: task["priority"])

        for task in self.tasks:
            self.create_task_row(task)

    def create_task_row(self, task):
        task_frame = tk.Frame(self.task_list_frame, bg="#F2CBFF")
        task_frame.pack(fill="x", pady=2)

        task_var = tk.StringVar(value=task["name"])
        task_label = tk.Label(task_frame, text=task["name"], width=40, anchor="w", font=("Courier New", 10))
        task_label.pack(side="left")

        task_label.bind("<Enter>", lambda e, task=task: self.show_task_details(task_label, task))
        task_label.bind("<Leave>", lambda e, task=task: self.hide_task_details(task_label))
        task_label.bind("<Button-1>", lambda e, task=task: self.edit_task(task))

        task_done = tk.IntVar()
        task_checkbox = tk.Checkbutton(task_frame, variable=task_done, command=lambda task=task, var=task_done: self.remove_task(task, var))
        task_checkbox.pack(side="right")

    def show_task_details(self, label, task):
        details = f"Due: {task['due_date']}, Priority: {task['priority']}"
        label.config(text=f"{task['name']} ({details})")

    def hide_task_details(self, label):
        label.config(text=label.cget("text").split(" (")[0])

    def remove_task(self, task, var):
        if var.get() == 1:
            self.tasks.remove(task)
            self.display_tasks()

    def edit_task(self, task):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Task")

    # Task name
        tk.Label(edit_window, text="Task Name:", font=("Courier New", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        task_name_var = tk.StringVar(value=task["name"])
        task_name_entry = tk.Entry(edit_window, textvariable=task_name_var, width=40, font=("Courier New", 10))
        task_name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Due date
        tk.Label(edit_window, text="Due Date:", font=("Courier New", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        due_date_var = tk.StringVar(value=task["due_date"].strftime('%Y-%m-%d'))
        due_date_entry = DateEntry(edit_window, textvariable=due_date_var, width=12, background='darkblue',
                                foreground='white', borderwidth=2, font=("Courier New", 10))
        due_date_entry.grid(row=1, column=1, padx=5, pady=5)
        due_date_entry.config(state="readonly")  # Disable editing

    # Priority
        tk.Label(edit_window, text="Priority:", font=("Courier New", 10)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        priority_var = tk.StringVar(value=str(task["priority"]))
        priority_dropdown = ttk.Combobox(edit_window, textvariable=priority_var, values=("1", "2", "3"), width=5, state="readonly", font=("Courier New", 10))
        priority_dropdown.grid(row=2, column=1, padx=5, pady=5)
        priority_dropdown.config(state="readonly")  # Disable editing

    # Save button
        def save_changes():
            task["name"] = task_name_var.get()
            task["due_date"] = self.parse_date(due_date_var.get())
            task["priority"] = int(priority_var.get())
            self.display_tasks()
            edit_window.destroy()

        save_button = tk.Button(edit_window, text="Save Changes", command=save_changes, font=("Courier New", 10))
        save_button.grid(row=3, column=0, columnspan=2, pady=10)

    def parse_date(self, date_string):
        try:
            return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
        except ValueError:
            try:
                return datetime.datetime.strptime(date_string, '%m/%d/%y').date()
            except ValueError:
                return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
