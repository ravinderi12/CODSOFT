#   Codesoft python internship project 1     to-do list 





import tkinter as tk
from tkinter import messagebox
import os
# Created by Ravinder - Simple To-Do App

# File to store tasks
FILE_NAME = "tasks.txt"

# Function to add a task
def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        save_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

#  to delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        save_tasks()
    else:
        messagebox.showinfo("Info", "Please select a task to delete.")

#  to mark task as completed
def mark_done():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        if not task.endswith(" ✅"):
            listbox.delete(selected)
            listbox.insert(selected, task + " ✅")
            save_tasks()

#  to save tasks to file
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + '\n')

#  to load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            for line in f:
                task = line.strip()
                if task:
                    listbox.insert(tk.END, task)

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x420")
root.config(bg="#007acc")  # Blue background


tk.Label(root, text="📋 My Task List", font=("Arial", 16, "bold"), bg="lightgray").pack(pady=10)


entry = tk.Entry(root, font=("Arial", 12), width=40)
entry.pack(pady=6)

tk.Button(root, text="Add Task  ➕", command=add_task, width=15).pack(pady=2)
tk.Button(root, text="Mark Done  ✅", command=mark_done, width=15).pack(pady=2)
tk.Button(root, text="Delete Task  🗑️", command=delete_task, width=15).pack(pady=2)

listbox = tk.Listbox(root, font=("Arial", 12), width=50, height=20)
listbox.pack(pady=12)

# Load saved tasks on start
load_tasks()

root.mainloop()

# Created by Ravinder  singh - Simple To-Do App
