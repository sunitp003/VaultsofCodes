import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    task_id = max([t['id'] for t in tasks], default=0) + 1  # Generate unique task ID
    tasks.append({"id": task_id, "task": task, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task}' added with ID {task_id}.")

def delete_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            save_tasks(tasks)
            print(f"Task with ID {task_id} deleted.")
            return
    print(f"Task with ID {task_id} not found.")

def delete_all_tasks():
    save_tasks([])
    print("All tasks have been deleted.")

def reset_all_tasks():
    tasks = load_tasks()
    for t in tasks:
        t["completed"] = False
    save_tasks(tasks)
    print("All tasks have been reset to incomplete.")

def reset_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = False
            save_tasks(tasks)
            print(f"Task with ID {task_id} has been reset to incomplete.")
            return
    print(f"Task with ID {task_id} not found.")

def display_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    print("\n" + "="*40)
    print("ID".ljust(5) + "Task".ljust(25) + "Status")
    print("-"*40)
    for idx, task in enumerate(tasks):
        status = "Complete" if task["completed"] else "Incomplete"
        print(f"{task['id']:<5}{task['task']:<25}{status}")
    print("="*40)

def mark_task_complete(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            save_tasks(tasks)
            print(f"Task with ID {task_id} marked as complete.")
            return
    print(f"Task with ID {task_id} not found.")
