# Task management
arr = []

while 1 :
    print("Select the operation : ")
    print("1) Add a task")
    print("2) Update a task")
    print("3) Remove a task")
    print("4) View tasks")
    print("5) Exit")

    opt = int(input("Enter your choice : "))

    if opt == 1 : 
        task = str(input("Enter the task to add in the list : "))
        arr.append(task)
        print("Task added to the list successfully")
    elif opt == 2 :
        print(arr)
        index = int(input("Enter index of the task you want to update : "))
        newTask = str(input("Enter the new task you want to update with : "))
        arr[index] = newTask
        print("Task updated to the list successfully")
    elif opt == 3 :
        # logic
        print("Task removed to the list successfully")
    elif opt == 4 :
        print(arr)
    else : break