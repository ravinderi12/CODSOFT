import json
import os

FILE_NAME = "todo_data.json"

# Load existing tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{idx}. {task['title']} [{status}]")

# Add task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added.")

# Mark complete
def complete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        deleted = tasks.pop(index)
        print(f"Deleted task: {deleted['title']}")
    else:
        print("Invalid task number.")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
