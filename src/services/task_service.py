import sqlite3
from datetime import date
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DATABASE_PATH = BASE_DIR / "data" / "project_management_portal.db"


def create_connection() -> sqlite3.Connection:
    """Create and return a SQLite database connection."""
    return sqlite3.connect(DATABASE_PATH)


def create_task(
    project_id: int,
    task_name: str,
    description: str,
    priority: str,
    status: str,
    assigned_to: str,
    due_date: str,
) -> None:
    """Insert a new task record into the tasks table."""
    query = """
    INSERT INTO tasks (
        project_id,
        task_name,
        description,
        priority,
        status,
        assigned_to,
        due_date,
        created_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """

    with create_connection() as connection:
        connection.execute(
            query,
            (
                project_id,
                task_name,
                description,
                priority,
                status,
                assigned_to,
                due_date,
                date.today().isoformat(),
            ),
        )
        connection.commit()


def get_tasks() -> list[tuple]:
    """Retrieve all task records from the tasks table."""
    query = """
    SELECT
        task_id,
        project_id,
        task_name,
        description,
        priority,
        status,
        assigned_to,
        due_date,
        created_date
    FROM tasks
    ORDER BY task_id;
    """

    with create_connection() as connection:
        cursor = connection.execute(query)
        return cursor.fetchall()


def update_task(
    task_id: int,
    task_name: str,
    description: str,
    priority: str,
    status: str,
    assigned_to: str,
    due_date: str,
) -> None:
    """Update an existing task record."""
    query = """
    UPDATE tasks
    SET
        task_name = ?,
        description = ?,
        priority = ?,
        status = ?,
        assigned_to = ?,
        due_date = ?
    WHERE task_id = ?;
    """

    with create_connection() as connection:
        connection.execute(
            query,
            (
                task_name,
                description,
                priority,
                status,
                assigned_to,
                due_date,
                task_id,
            ),
        )
        connection.commit()


def delete_task(task_id: int) -> None:
    """Delete an existing task record."""
    query = """
    DELETE FROM tasks
    WHERE task_id = ?;
    """

    with create_connection() as connection:
        connection.execute(query, (task_id,))
        connection.commit()


if __name__ == "__main__":
    with create_connection() as connection:
        connection.execute("DELETE FROM tasks;")
        connection.execute("DELETE FROM sqlite_sequence WHERE name='tasks';")
        connection.commit()

    create_task(
        project_id=1,
        task_name="Create Database Schema",
        description="Build the initial projects and tasks database tables.",
        priority="High",
        status="Complete",
        assigned_to="Vincent Castillo",
        due_date="2026-06-12",
    )

    create_task(
        project_id=1,
        task_name="Create Project CRUD Operations",
        description="Implement create, read, update, and delete operations for projects.",
        priority="High",
        status="Complete",
        assigned_to="Vincent Castillo",
        due_date="2026-06-12",
    )

    create_task(
        project_id=1,
        task_name="Create Streamlit Project Viewer",
        description="Display project records in a Streamlit browser interface.",
        priority="Medium",
        status="Complete",
        assigned_to="Vincent Castillo",
        due_date="2026-06-12",
    )

    create_task(
        project_id=1,
        task_name="Create Task CRUD Operations",
        description="Implement create, read, update, and delete operations for tasks.",
        priority="High",
        status="In Progress",
        assigned_to="Vincent Castillo",
        due_date="2026-06-12",
    )

    update_task(
        task_id=4,
        task_name="Create Task CRUD Operations",
        description="Implement create, read, update, and delete operations for tasks.",
        priority="High",
        status="Complete",
        assigned_to="Vincent Castillo",
        due_date="2026-06-12",
    )

    delete_task(task_id=3)

    tasks = get_tasks()

    for task in tasks:
        print(task)