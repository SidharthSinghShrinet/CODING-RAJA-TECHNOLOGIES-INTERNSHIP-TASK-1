# Imports
import os

# Task class to store task details
class Task:
  def __init__(self, description, priority, due_date, is_completed):
    self.description = description
    self.priority = priority
    self.due_date = due_date
    self.is_completed = is_completed

  def __str__(self):
    return f"[{'Completed' if self.is_completed else 'Pending'}] {self.priority.upper()} - {self.description} (Due: {self.due_date})"

# Function to load tasks from a file
def load_tasks():
  tasks = []
  if os.path.exists("tasks.dat"):
    with open("tasks.dat", "r") as file:
      for line in file:
        data = line.strip().split(",")
        tasks.append(Task(data[0], data[1], data[2], data[3] == "True"))
  return tasks

# Function to save tasks to a file
def save_tasks(tasks):
  with open("tasks.dat", "w") as file:
    for task in tasks:
      data = [task.description, task.priority, task.due_date, str(task.is_completed)]
      file.write(",".join(data) + "\n")

# Main program loop
def main():
  tasks = load_tasks()

  while True:
    print("\n** To-Do List App**")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Remove Task")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
      description = input("Enter task description: ")
      priority = input("Enter priority (high, medium, low): ")
      due_date = input("Enter due date (YYYY-MM-DD) (optional): ")
      tasks.append(Task(description, priority, due_date, False))
      print("Task added successfully!")
    elif choice == "2":
      if not tasks:
        print("No tasks found!")
      else:
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")
    elif choice == "3":
      if not tasks:
        print("No tasks found!")
      else:
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")
        index = int(input("Enter the number of the task to mark complete: ")) - 1
        if 0 <= index < len(tasks):
          tasks[index].is_completed = True
          print("Task marked complete!")
        else:
          print("Invalid task number!")
    elif choice == "4":
      if not tasks:
        print("No tasks found!")
      else:
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
          del tasks[index]
          print("Task removed successfully!")
        else:
          print("Invalid task number!")
    elif choice == "5":
      save_tasks(tasks)
      print("Exiting...")
      break
    else:
      print("Invalid choice!")

if __name__ == "__main__":
  main()
