def display_menu():
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task(todo_list):
    task = input("Enter task: ")
    todo_list.append(task)
    print(f'Task "{task}" added successfully.')

def remove_task(todo_list):
    task = input("Enter task to remove: ")
    if task in todo_list:
        todo_list.remove(task)
        print(f'Task "{task}" removed successfully.')
    else:
        print("Task not found.")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Your Tasks:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            remove_task(todo_list)
        elif choice == "3":
            view_tasks(todo_list)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
