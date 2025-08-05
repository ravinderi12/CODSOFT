import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# File to store contacts
file_name = "contacts.csv"

# If file doesn't exist, create it with headers
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Address"])

# Functions
def save_contact():
    name = name_input.get()
    phone = phone_input.get()
    email = email_input.get()
    address = address_input.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required fields.")
        return

    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email, address])

    messagebox.showinfo("Saved", "Contact added successfully.")
    clear_inputs()
    show_all_contacts()

def show_all_contacts():
    contact_list.delete(*contact_list.get_children())
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            contact_list.insert("", tk.END, values=row)

def search_contact():
    search = search_input.get().lower()
    contact_list.delete(*contact_list.get_children())

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if search in row[0].lower() or search in row[1]:
                contact_list.insert("", tk.END, values=row)

def select_item(event):
    selected = contact_list.focus()
    values = contact_list.item(selected, 'values')
    if values:
        name_input.set(values[0])
        phone_input.set(values[1])
        email_input.set(values[2])
        address_input.set(values[3])

def update_contact():
    selected = contact_list.focus()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to update.")
        return

    new_data = [name_input.get(), phone_input.get(), email_input.get(), address_input.get()]
    old_data = contact_list.item(selected, "values")

    with open(file_name, "r") as f:
        rows = list(csv.reader(f))

    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            if row == list(old_data):
                writer.writerow(new_data)
            else:
                writer.writerow(row)

    messagebox.showinfo("Updated", "Contact updated successfully.")
    clear_inputs()
    show_all_contacts()

def delete_contact():
    selected = contact_list.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a contact to delete.")
        return

    to_delete = contact_list.item(selected, "values")

    with open(file_name, "r") as f:
        rows = list(csv.reader(f))

    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            if row != list(to_delete):
                writer.writerow(row)

    messagebox.showinfo("Deleted", "Contact deleted successfully.")
    clear_inputs()
    show_all_contacts()

def clear_inputs():
    name_input.set("")
    phone_input.set("")
    email_input.set("")
    address_input.set("")
    search_input.set("")
    contact_list.selection_remove(contact_list.selection())

# GUI Start
root = tk.Tk()
root.title("My Contact Book")
root.geometry("800x500")
root.configure(bg="#eef1f5")
root.resizable(False, False)

# Input variables
name_input = tk.StringVar()
phone_input = tk.StringVar()
email_input = tk.StringVar()
address_input = tk.StringVar()
search_input = tk.StringVar()

# Frame for input
input_frame = tk.LabelFrame(root, text="Add / Edit Contact", bg="#eef1f5", font=("Segoe UI", 11, "bold"))
input_frame.pack(fill="x", padx=10, pady=10)

tk.Label(input_frame, text="Name:", bg="#eef1f5").grid(row=0, column=0)
tk.Entry(input_frame, textvariable=name_input, width=25).grid(row=0, column=1, padx=10)

tk.Label(input_frame, text="Phone:", bg="#eef1f5").grid(row=0, column=2)
tk.Entry(input_frame, textvariable=phone_input, width=25).grid(row=0, column=3, padx=10)

tk.Label(input_frame, text="Email:", bg="#eef1f5").grid(row=1, column=0)
tk.Entry(input_frame, textvariable=email_input, width=25).grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Address:", bg="#eef1f5").grid(row=1, column=2)
tk.Entry(input_frame, textvariable=address_input, width=25).grid(row=1, column=3, padx=10, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#eef1f5")
btn_frame.pack(pady=5)

ttk.Button(btn_frame, text="Add", width=12, command=save_contact).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Update", width=12, command=update_contact).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Delete", width=12, command=delete_contact).grid(row=0, column=2, padx=5)
ttk.Button(btn_frame, text="Clear", width=12, command=clear_inputs).grid(row=0, column=3, padx=5)

# Search
search_frame = tk.Frame(root, bg="#eef1f5")
search_frame.pack(pady=5)

tk.Entry(search_frame, textvariable=search_input, width=35).grid(row=0, column=0, padx=5)
ttk.Button(search_frame, text="Search", command=search_contact).grid(row=0, column=1)
ttk.Button(search_frame, text="Show All", command=show_all_contacts).grid(row=0, column=2, padx=5)

# Table
table_frame = tk.Frame(root)
table_frame.pack(padx=10, pady=10, fill="both", expand=True)

scroll = tk.Scrollbar(table_frame)
scroll.pack(side="right", fill="y")

contact_list = ttk.Treeview(table_frame, columns=("Name", "Phone", "Email", "Address"), show='headings', yscrollcommand=scroll.set)
contact_list.heading("Name", text="Name")
contact_list.heading("Phone", text="Phone")
contact_list.heading("Email", text="Email")
contact_list.heading("Address", text="Address")

contact_list.column("Name", width=150)
contact_list.column("Phone", width=120)
contact_list.column("Email", width=180)
contact_list.column("Address", width=250)

contact_list.bind("<ButtonRelease-1>", select_item)
contact_list.pack(fill="both", expand=True)
scroll.config(command=contact_list.yview)

# Load contacts at start
show_all_contacts()

# Start GUI
root.mainloop()
