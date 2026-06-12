import sqlite3
from datetime import date
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DATABASE_PATH = BASE_DIR / "data" / "project_management_portal.db"


def create_connection() -> sqlite3.Connection:
    """Create and return a SQLite database connection."""
    return sqlite3.connect(DATABASE_PATH)


def create_project(project_name: str, description: str, status: str = "Active") -> None:
    """Insert a new project record into the projects table."""
    query = """
    INSERT INTO projects (
        project_name,
        description,
        status,
        created_date
    )
    VALUES (?, ?, ?, ?);
    """

    with create_connection() as connection:
        connection.execute(
            query,
            (
                project_name,
                description,
                status,
                date.today().isoformat(),
            ),
        )
        connection.commit()


def get_projects() -> list[tuple]:
    """Retrieve all project records from the projects table."""
    query = """
    SELECT
        project_id,
        project_name,
        description,
        status,
        created_date
    FROM projects
    ORDER BY project_id;
    """

    with create_connection() as connection:
        cursor = connection.execute(query)
        return cursor.fetchall()

def update_project(
    project_id: int,
    project_name: str,
    description: str,
    status: str,
) -> None:
    """Update an existing project record."""
    query = """
    UPDATE projects
    SET
        project_name = ?,
        description = ?,
        status = ?
    WHERE project_id = ?;
    """

    with create_connection() as connection:
        connection.execute(
            query,
            (
                project_name,
                description,
                status,
                project_id,
            ),
        )
        connection.commit()


def delete_project(project_id: int) -> None:
    """Delete an existing project record."""
    query = """
    DELETE FROM projects
    WHERE project_id = ?;
    """

    with create_connection() as connection:
        connection.execute(query, (project_id,))
        connection.commit()

if __name__ == "__main__":
    with create_connection() as connection:
        connection.execute("DELETE FROM projects;")
        connection.execute("DELETE FROM sqlite_sequence WHERE name='projects';")
        connection.commit()

    create_project(
        project_name="Project Management Portal",
        description="Full-stack project management application for tracking projects and tasks.",
        status="Active",
    )

    create_project(
        project_name="AI Knowledge Assistant",
        description="AI-powered assistant for document search and question answering.",
        status="Planning",
    )

    create_project(
        project_name="Cloud Deployment Platform",
        description="Containerized application deployment project using Docker and cloud services.",
        status="Planning",
    )

    update_project(
        project_id=2,
        project_name="AI Knowledge Assistant",
        description="AI-powered assistant for document search, retrieval, and question answering.",
        status="Active",
    )

    delete_project(project_id=3)

    projects = get_projects()

    for project in projects:
        print(project)