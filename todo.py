def task():
    tasks = []  # empty list
    print("welcome to the Task manager  app")

    total_task = int(input("enter how many tasks you want to add: "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"today's tasks are: {tasks}")

    while True:
        print("\nChoose an operation:")
        print("1 - add")
        print("2 - update")
        print("3 - delete")
        print("4 - view")
        print("5 - exit")

        operation = int(input("enter your choice: "))

        if operation == 1:
            add = input("enter task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been added succesfully ")

        elif operation == 2:
            updated_val = input("enter the task you want to update: ")

            if updated_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"task updated to '{up}'.")
            else:
                print("task not found!")

        elif operation == 3:
            del_val = input("Enter task  to delete: ")

            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' has been deleted")
            else:
                print("Task not found!")

        elif operation == 4:
            print(f"Total tasks: {tasks}")

        elif operation == 5:
            print("Closing the Task Manageer")
            break

        else:
            print("Invalid input")

# Runing  the function
task()
