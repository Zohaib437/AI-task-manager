# ai_task_manager_online.py
import sqlite3

class TaskManager:
    def __init__(self):
        # Use in-memory database for online compilers
        self.conn = sqlite3.connect(":memory:")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            status TEXT DEFAULT 'Pending'
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_task(self, title, description, due_date):
        query = "INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)"
        self.conn.execute(query, (title, description, due_date))
        self.conn.commit()

    def update_status(self, task_id, status):
        query = "UPDATE tasks SET status = ? WHERE id = ?"
        self.conn.execute(query, (status, task_id))
        self.conn.commit()

    def list_tasks(self):
        cursor = self.conn.execute("SELECT * FROM tasks")
        for row in cursor:
            print(f"ID: {row[0]}, Title: {row[1]}, Due: {row[3]}, Status: {row[4]}")

    def delete_task(self, task_id):
        query = "DELETE FROM tasks WHERE id = ?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()


if __name__ == "__main__":
    manager = TaskManager()

    # Add sample tasks
    manager.add_task("Finish Codex Application", "Complete the OpenAI form", "2026-03-15")
    manager.add_task("Prepare Presentation", "Slides for CS114 project", "2026-03-20")

    print("All Tasks:")
    manager.list_tasks()

    print("\nUpdating status of Task 1...")
    manager.update_status(1, "Completed")

    print("\nAll Tasks after update:")
    manager.list_tasks()
