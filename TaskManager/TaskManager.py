import pandas as pd

try:
    df = pd.read_csv("tasks.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Task ID", "Task Name", "Description", "Status"])

def add_task(task_name, description):
    """
    Adds a new task to the task list.

    Parameters:
    - task_name (str): The name of the task.
    - description (str): A brief description of the task.
    """
    global df
    new_task_id = len(df) + 1
    new_task = {"Task ID": new_task_id, "Task Name": task_name, "Description": description, "Status": "Incomplete"}
    df = pd.concat([df, pd.DataFrame([new_task])], ignore_index=True)
    df.to_csv("tasks.csv", index=False)
    print("Task added successfully!")

def view_tasks():
    """
    Displays all tasks.
    """
    global df
    if df.empty:
        print("No tasks available.")
    else:
        print("Current Tasks:")
        print(df)

def update_task(task_id, new_name=None, new_description=None):
    """
    Updates an existing task's name or description.

    Parameters:
    - task_id (int): The ID of the task to update.
    - new_name (str): The new name for the task.
    - new_description (str): The new description for the task.
    """
    global df
    if task_id in df["Task ID"].values:
        if new_name:
            df.loc[df["Task ID"] == task_id, "Task Name"] = new_name
        if new_description:
            df.loc[df["Task ID"] == task_id, "Description"] = new_description
        df.to_csv("tasks.csv", index=False)
        print("Task updated successfully!")
    else:
        print("Task ID not found.")

def delete_task(task_id):
    """
    Deletes a task by its ID.

    Parameters:
    - task_id (int): The ID of the task to delete.
    """
    global df
    if task_id in df["Task ID"].values:
        df = df[df["Task ID"] != task_id]
        df.to_csv("tasks.csv", index=False)
        print("Task deleted successfully!")
    else:
        print("Task ID not found.")

def mark_task_completed(task_id):
    """
    Marks a task as completed by changing its status.

    Parameters:
    - task_id (int): The ID of the task to mark as completed.
    """
    global df
    if task_id in df["Task ID"].values:
        df.loc[df["Task ID"] == task_id, "Status"] = "Completed"
        df.to_csv("tasks.csv", index=False)
        print("Task marked as completed!")
    else:
        print("Task ID not found.")

def main():
    """
    The main function to run the script. It provides a menu for the user to select different actions.
    """
    while True:
        print("\nMenu:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as completed")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            task_name = input("Enter the task name: ")
            description = input("Enter the task description: ")
            add_task(task_name, description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter the task ID to update: "))
                new_name = input("Enter the new name (leave blank to keep current): ")
                new_description = input("Enter the new description (leave blank to keep current): ")
                update_task(task_id, new_name or None, new_description or None)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif choice == '4':
            try:
                task_id = int(input("Enter the task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif choice == '5':
            try:
                task_id = int(input("Enter the task ID to mark as completed: "))
                mark_task_completed(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select an option from the menu.")

if __name__ == "__main__":
    main()
