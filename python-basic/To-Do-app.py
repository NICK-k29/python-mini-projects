def task():
    tasks = [] #empty list
    print("---WELCOME TO THE TO-DO APP---")

    total_task =int(input("Enter how many task you want to add = ")) #5
    for i  in range(1, total_task+1):
        task_name = input(f"Enter the task {i} = ")   #enter 3 task
        tasks.append(task_name)

    print(f"Today's task are\n{tasks}")

    while True:
        operation = int(input("Enter \n1-Add\n2-update\n3-delete\n4-view\n5-exit"))
        if operation == 1:
            add = input("Enter the task you want add = ")
            tasks.append(add)
            print(f"Task {add} added successfully added...\n")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task updeted successfully... {up}")

        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                tasks.pop(ind)
                print(f"Task {del_val} has been deleted successfully...\n")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("Closing the Program...")
            break

        else:
            print("Invalid input")

task()