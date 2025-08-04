import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "tasks.json"

# Load tasks from JSON
def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

# Save tasks to JSON
def save_tasks():
    with open(DATA_FILE, 'w') as f:
        json.dump(task_list, f)

# Refresh the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in task_list:
        status = "✓" if task['done'] else "✗"
        listbox.insert(tk.END, f"{task['title']} [{status}]")

# Add a task
def add_task():
    title = entry.get().strip()
    if title:
        task_list.append({'title': title, 'done': False})
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Mark selected task as done
def mark_done():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        task_list[idx]['done'] = True
        update_listbox()
    else:
        messagebox.showinfo("Info", "Select a task to mark as done.")

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        del task_list[idx]
        update_listbox()
    else:
        messagebox.showinfo("Info", "Select a task to delete.")

# On app close
def on_close():
    save_tasks()
    root.destroy()

# Initialize main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.resizable(False, False)

# Load task list
task_list = load_tasks()

# Entry field
entry = tk.Entry(root, width=30, font=('Arial', 12))
entry.pack(pady=10)

# Add button
add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

# Listbox for tasks
listbox = tk.Listbox(root, width=40, height=10, font=('Arial', 12))
listbox.pack(pady=10)
update_listbox()

# Buttons for Done & Delete
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

done_btn = tk.Button(btn_frame, text="Mark Done", width=15, command=mark_done)
done_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", width=15, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

# Handle window close
root.protocol("WM_DELETE_WINDOW", on_close)

# Start GUI loop
root.mainloop()
