import os

# Global task list
tasks = []

# Function to add a task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)
    print("Task added successfully!")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks):
        print(f"Task ID: {i}, Title: {task['title']}, Description: {task['description']}, Completed: {task['completed']}")

# Function to mark a task as complete or uncompleted
def mark_task():
    task_id = int(input("Enter task ID to mark as complete/uncompleted: "))
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
        print("Task marked as complete/uncompleted.")
    else:
        print("Invalid task ID!")

# Function to delete a task
def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
        print("Task deleted successfully.")
    else:
        print("Invalid task ID!")

# Function to save tasks to a text file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['title']},{task['description']},{task['completed']}\n")
    print("Tasks saved to file.")

# Function to load tasks from a text file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                title, description, completed = line.strip().split(',')
                tasks.append({"title": title, "description": description, "completed": completed == "True"})
        print("Tasks loaded from file.")

# Main program loop
def main():
    load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete/Uncompleted")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            mark_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            save_tasks()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
