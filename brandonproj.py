def clear_screen():
    print('\n' * 5)

# Function to add a task to the list
def add_task(tasks, title):
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added.")

# Function to mark a task as completed
def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"Task '{tasks[index]['title']}' marked as completed.")
    else:
        print("Invalid task index.")

# Function to list all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index + 1}. {task['title']} - {status}")

# Function to save tasks to a file
def save_tasks(tasks, filename):
    try:
        with open(filename, 'w') as f:
            for task in tasks:
                f.write(f"{task['title']},{task['completed']}\n")
        print(f"Tasks saved to '{filename}'.")
    except Exception as e:
        print(f"Failed to save tasks: {e}")

# Function to load tasks from a file
def load_tasks(filename):
    tasks = []
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                for line in f:
                    title, completed = line.strip().split(',')
                    tasks.append({"title": title, "completed": bool(int(completed))})
            print(f"Tasks loaded from '{filename}'.")
    except Exception as e:
        print(f"Failed to load tasks: {e}")
    return tasks

# Main function to run the to-do list manager
def main():
    tasks = []
    tasks_file = "tasks.txt"  # Change this to a desired filename

    # Load tasks from file if exists
    tasks = load_tasks(tasks_file)

    while True:
        clear_screen()
        print("To-Do List Manager")
        print("------------------")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. List Tasks")
        print("4. Save Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(tasks, title)
        elif choice == '2':
            list_tasks(tasks)
            try:
                index = int(input("Enter task index to mark as completed: ")) - 1
                complete_task(tasks, index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            list_tasks(tasks)
            input("Press Enter to continue...")
        elif choice == '4':
            save_tasks(tasks, tasks_file)
            input("Tasks saved. Press Enter to continue...")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")
            input("Press Enter to continue...")

    # Save tasks before exiting
    save_tasks(tasks, tasks_file)

#if __name__ == "__main__":
main()
   

    