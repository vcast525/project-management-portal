import requests
import streamlit as st


API_BASE_URL = "http://127.0.0.1:8000"


def fetch_projects() -> list[dict]:
    """Fetch project records from FastAPI."""
    response = requests.get(f"{API_BASE_URL}/projects")
    response.raise_for_status()
    return response.json()


def fetch_tasks() -> list[dict]:
    """Fetch task records from FastAPI."""
    response = requests.get(f"{API_BASE_URL}/tasks")
    response.raise_for_status()
    return response.json()


def create_project(project_name: str, description: str, status: str) -> None:
    """Create a new project through FastAPI."""
    payload = {
        "project_name": project_name,
        "description": description,
        "status": status,
    }

    response = requests.post(f"{API_BASE_URL}/projects", json=payload)
    response.raise_for_status()


def create_task(
    project_id: int,
    task_name: str,
    description: str,
    priority: str,
    status: str,
    assigned_to: str,
    due_date: str,
) -> None:
    """Create a new task through FastAPI."""
    payload = {
        "project_id": project_id,
        "task_name": task_name,
        "description": description,
        "priority": priority,
        "status": status,
        "assigned_to": assigned_to,
        "due_date": due_date,
    }

    response = requests.post(f"{API_BASE_URL}/tasks", json=payload)
    response.raise_for_status()


def update_project(
    project_id: int,
    project_name: str,
    description: str,
    status: str,
) -> None:
    """Update an existing project through FastAPI."""
    payload = {
        "project_name": project_name,
        "description": description,
        "status": status,
    }

    response = requests.put(f"{API_BASE_URL}/projects/{project_id}", json=payload)
    response.raise_for_status()


def update_task(
    task_id: int,
    project_id: int,
    task_name: str,
    description: str,
    priority: str,
    status: str,
    assigned_to: str,
    due_date: str,
) -> None:
    """Update an existing task through FastAPI."""
    payload = {
        "project_id": project_id,
        "task_name": task_name,
        "description": description,
        "priority": priority,
        "status": status,
        "assigned_to": assigned_to,
        "due_date": due_date,
    }

    response = requests.put(f"{API_BASE_URL}/tasks/{task_id}", json=payload)
    response.raise_for_status()


def delete_task(task_id: int) -> None:
    """Delete an existing task through FastAPI."""
    response = requests.delete(f"{API_BASE_URL}/tasks/{task_id}")
    response.raise_for_status()


st.set_page_config(
    page_title="Project Management Portal",
    page_icon="📋",
    layout="wide",
)

st.title("📋 Project Management Portal")

projects = fetch_projects()
tasks = fetch_tasks()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Total Projects",
        value=len(projects),
    )

with col2:
    st.metric(
        label="Total Tasks",
        value=len(tasks),
    )

st.divider()

st.header("Create Records")

with st.expander("Create New Project"):
    with st.form("create_project_form"):
        project_name = st.text_input("Project Name")
        project_description = st.text_area("Project Description")
        project_status = st.selectbox(
            "Project Status",
            ["Planning", "Active", "Complete", "On Hold"],
        )

        submitted_project = st.form_submit_button("Create Project")

        if submitted_project:
            create_project(
                project_name=project_name,
                description=project_description,
                status=project_status,
            )
            st.success("Project created successfully. Refresh the page to see updates.")

with st.expander("Create New Task"):
    with st.form("create_task_form"):
        project_options = {
            f"{project['project_id']} - {project['project_name']}": project["project_id"]
            for project in projects
        }

        selected_project = st.selectbox(
            "Project",
            list(project_options.keys()),
        )

        task_name = st.text_input("Task Name")
        task_description = st.text_area("Task Description")
        task_priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
        task_status = st.selectbox(
            "Task Status",
            ["Planning", "In Progress", "Complete", "Blocked"],
        )
        assigned_to = st.text_input("Assigned To")
        due_date = st.date_input("Due Date")

        submitted_task = st.form_submit_button("Create Task")

        if submitted_task:
            create_task(
                project_id=project_options[selected_project],
                task_name=task_name,
                description=task_description,
                priority=task_priority,
                status=task_status,
                assigned_to=assigned_to,
                due_date=due_date.isoformat(),
            )
            st.success("Task created successfully. Refresh the page to see updates.")

st.divider()

st.header("Update Records")

with st.expander("Update Project Status"):
    if projects:
        project_update_options = {
            f"{project['project_id']} - {project['project_name']}": project
            for project in projects
        }

        selected_project_update = st.selectbox(
            "Select Project To Update",
            list(project_update_options.keys()),
        )

        selected_project_data = project_update_options[selected_project_update]

        updated_project_status = st.selectbox(
            "Updated Project Status",
            ["Planning", "Active", "Complete", "On Hold"],
        )

        if st.button("Update Project Status"):
            update_project(
                project_id=selected_project_data["project_id"],
                project_name=selected_project_data["project_name"],
                description=selected_project_data["description"],
                status=updated_project_status,
            )
            st.success("Project status updated successfully. Refresh the page to see updates.")

with st.expander("Update Task Status"):
    if tasks:
        task_update_options = {
            f"{task['task_id']} - {task['task_name']}": task
            for task in tasks
        }

        selected_task_update = st.selectbox(
            "Select Task To Update",
            list(task_update_options.keys()),
        )

        selected_task_data = task_update_options[selected_task_update]

        updated_task_status = st.selectbox(
            "Updated Task Status",
            ["Planning", "In Progress", "Complete", "Blocked"],
        )

        if st.button("Update Task Status"):
            update_task(
                task_id=selected_task_data["task_id"],
                project_id=selected_task_data["project_id"],
                task_name=selected_task_data["task_name"],
                description=selected_task_data["description"],
                priority=selected_task_data["priority"],
                status=updated_task_status,
                assigned_to=selected_task_data["assigned_to"],
                due_date=selected_task_data["due_date"],
            )
            st.success("Task status updated successfully. Refresh the page to see updates.")

st.divider()

st.header("Delete Records")

with st.expander("Delete Task"):
    if tasks:
        task_delete_options = {
            f"{task['task_id']} - {task['task_name']}": task["task_id"]
            for task in tasks
        }

        selected_task_delete = st.selectbox(
            "Select Task To Delete",
            list(task_delete_options.keys()),
        )

        if st.button("Delete Task"):
            delete_task(task_delete_options[selected_task_delete])
            st.success("Task deleted successfully. Refresh the page to see updates.")

st.divider()

st.header("Projects")

for project in projects:
    name = project["project_name"]
    description = project["description"]
    status = project["status"]
    created_date = project["created_date"]

    with st.container():
        st.markdown(f"### {name}")
        st.write(f"**Status:** {status}")
        st.write(f"**Description:** {description}")
        st.write(f"**Created Date:** {created_date}")
        st.divider()

st.header("Tasks")

for task in tasks:
    task_name = task["task_name"]
    description = task["description"]
    priority = task["priority"]
    status = task["status"]
    assigned_to = task["assigned_to"]
    due_date = task["due_date"]

    with st.container():
        st.markdown(f"### {task_name}")
        st.write(f"**Priority:** {priority}")
        st.write(f"**Status:** {status}")
        st.write(f"**Assigned To:** {assigned_to}")
        st.write(f"**Due Date:** {due_date}")
        st.write(f"**Description:** {description}")
        st.divider()