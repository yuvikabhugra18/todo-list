import sqlite3

# connect to database (file will auto-create)
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
)
""")
conn.commit()

def add_task():
    task = input("Enter task: ")
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    print("Task added!")

def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    if not rows:
        print("\nNo tasks found!")
        return

    print("\n--- Your Tasks ---")
    for row in rows:
        print(f"{row[0]}. {row[1]}")

def delete_task():
    view_tasks()
    try:
        task_id = int(input("Enter task ID to delete: "))
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        print("Task deleted!")
    except ValueError:
        print("Enter a valid number!")

def menu():
    while True:
        print("\n--- TO-DO LIST (SQL) ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

menu()
conn.close()
