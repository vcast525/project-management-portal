import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "project_management_portal.db"


def create_connection() -> sqlite3.Connection:
    """Create and return a SQLite database connection."""
    DATA_DIR.mkdir(exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)


def create_projects_table(connection: sqlite3.Connection) -> None:
    """Create the projects table."""
    query = """
    CREATE TABLE IF NOT EXISTS projects (
        project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT NOT NULL,
        description TEXT,
        status TEXT NOT NULL,
        created_date TEXT NOT NULL
    );
    """
    connection.execute(query)


def create_tasks_table(connection: sqlite3.Connection) -> None:
    """Create the tasks table."""
    query = """
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        task_name TEXT NOT NULL,
        description TEXT,
        priority TEXT NOT NULL,
        status TEXT NOT NULL,
        assigned_to TEXT,
        due_date TEXT,
        created_date TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects(project_id)
    );
    """
    connection.execute(query)


def initialize_database() -> None:
    """Initialize the Project Management Portal database schema."""
    with create_connection() as connection:
        create_projects_table(connection)
        create_tasks_table(connection)
        connection.commit()

    print(f"Database initialized successfully: {DATABASE_PATH}")


if __name__ == "__main__":
    initialize_database()