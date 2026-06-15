import sys
from pathlib import Path

import streamlit as st
import requests

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

sys.path.append(str(Path(__file__).resolve().parents[2]))

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
        value=len(projects)
    )

with col2:
    st.metric(
        label="Total Tasks",
        value=len(tasks)
    )

st.divider()

st.subheader("Projects")

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

st.subheader("Tasks")

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