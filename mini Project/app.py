from functions import add_task, delete_task, delete_all_tasks, display_tasks, mark_task_complete, reset_all_tasks, reset_task

def show_menu():
    print("\n" + "="*40)
    print("To-Do List Application".center(40))
    print("="*40)
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Display Tasks")
    print("4. Mark Task(s) as Complete")
    print("5. Reset All Tasks to Incomplete")
    print("6. Delete All Tasks")
    print("7. Reset a Particular Task")
    print("8. Exit")
    print("="*40)

def mark_multiple_tasks_complete():
    while True:
        display_tasks()
        task_ids = input("Enter task IDs to mark as complete (comma-separated), or 'exit' to return to menu: ")
        if task_ids.lower() == 'exit':
            break
        try:
            task_ids = [int(tid.strip()) for tid in task_ids.split(",")]
            for task_id in task_ids:
                mark_task_complete(task_id)
        except ValueError:
            print("Invalid input. Please enter valid task IDs.")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                task = input("Enter a task (or type 'exit' to return to menu): ")
                if task.lower() == 'exit':
                    break
                add_task(task)
            continue  # Continue to show the menu after adding tasks

        elif choice == '2':
            display_tasks()
            try:
                task_id = int(input("Enter the task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == '3':
            display_tasks()

        elif choice == '4':
            mark_multiple_tasks_complete()

        elif choice == '5':
            reset_all_tasks()

        elif choice == '6':
            delete_all_tasks()

        elif choice == '7':
            display_tasks()
            try:
                task_id = int(input("Enter the task ID to reset: "))
                reset_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")

        elif choice == '8':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")
    
    input("Press Enter to exit...")
