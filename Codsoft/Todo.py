import tkinter as tk
from tkinter import simpledialog, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame,
            width=50,
            height=10,
            selectmode=tk.SINGLE,
            font=("Helvetica", 12)
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, font=("Helvetica", 12))
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(
            self.button_frame,
            text="Add Task",
            width=15,
            command=self.add_task
        )
        self.add_button.grid(row=0, column=0, padx=5)

        self.update_button = tk.Button(
            self.button_frame,
            text="Update Task",
            width=15,
            command=self.update_task
        )
        self.update_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(
            self.button_frame,
            text="Delete Task",
            width=15,
            command=self.delete_task
        )
        self.delete_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            updated_task = simpledialog.askstring("Update Task", "Update the task:", initialvalue=self.tasks[selected_task_index])
            if updated_task:
                self.tasks[selected_task_index] = updated_task
                self.update_listbox()
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
