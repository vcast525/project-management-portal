import sys
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.services.project_service import get_projects, get_project_by_id
from src.services.task_service import create_task, get_task_by_id, get_tasks

app = FastAPI(
    title="Project Management Portal API",
    description="REST API for retrieving project and task data from the Project Management Portal.",
    version="1.0.0",
)

class TaskCreate(BaseModel):
    project_id: int
    task_name: str
    description: str
    priority: str
    status: str
    assigned_to: str
    due_date: str

@app.get("/")
def root() -> dict:
    """Root endpoint for API health check."""
    return {
        "message": "Project Management Portal API is running"
    }

@app.get("/projects")
def read_projects() -> list[dict]:
    """Retrieve all project records."""
    projects = get_projects()

    return [
        {
            "project_id": project[0],
            "project_name": project[1],
            "description": project[2],
            "status": project[3],
            "created_date": project[4],
        }
        for project in projects
    ]

@app.get("/projects/{project_id}")
def read_project(project_id: int) -> dict:
    """Retrieve a single project record by project ID."""
    project = get_project_by_id(project_id)

    if project is None:
        return {
            "error": "Project not found"
        }

    return {
        "project_id": project[0],
        "project_name": project[1],
        "description": project[2],
        "status": project[3],
        "created_date": project[4],
    }

@app.post("/tasks")
def create_task_endpoint(task: TaskCreate) -> dict:
    """Create a new task record."""
    create_task(
        project_id=task.project_id,
        task_name=task.task_name,
        description=task.description,
        priority=task.priority,
        status=task.status,
        assigned_to=task.assigned_to,
        due_date=task.due_date,
    )

    return {
        "message": "Task created successfully",
        "task_name": task.task_name,
    }

@app.get("/tasks")
def read_tasks() -> list[dict]:
    """Retrieve all task records."""
    tasks = get_tasks()

    return [
        {
            "task_id": task[0],
            "project_id": task[1],
            "task_name": task[2],
            "description": task[3],
            "priority": task[4],
            "status": task[5],
            "assigned_to": task[6],
            "due_date": task[7],
            "created_date": task[8],
        }
        for task in tasks
    ]
@app.get("/tasks/{task_id}")
def read_task(task_id: int) -> dict:
    """Retrieve a single task record by task ID."""
    task = get_task_by_id(task_id)

    if task is None:
        return {
            "error": "Task not found"
        }

    return {
        "task_id": task[0],
        "project_id": task[1],
        "task_name": task[2],
        "description": task[3],
        "priority": task[4],
        "status": task[5],
        "assigned_to": task[6],
        "due_date": task[7],
        "created_date": task[8],
    }
