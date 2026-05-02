from manager import ToDoManager
from file_handler import save_tasks_to_csv, load_tasks_from_csv, save_summary_to_txt


def main():
    manager = ToDoManager()
    manager.tasks = load_tasks_from_csv()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Show Tasks")
        print("4. Mark Task Completed")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter priority (low/medium/high): ")
            manager.add_task(title, priority)
            print("Task added!")

        elif choice == "2":
            title = input("Enter task title to delete: ")
            if manager.delete_task(title):
                print("Task deleted!")
            else:
                print("Task not found.")

        elif choice == "3":
            manager.show_tasks()

        elif choice == "4":
            title = input("Enter task title to mark as completed: ")
            if manager.mark_task_completed(title):
                print("Task marked as completed!")
            else:
                print("Task not found.")

        elif choice == "5":
            save_tasks_to_csv(manager.tasks)
            save_summary_to_txt(manager.tasks)
            print("Tasks saved to CSV and TXT. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()