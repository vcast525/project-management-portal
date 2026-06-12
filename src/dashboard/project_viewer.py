import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.services.project_service import get_projects
from src.services.task_service import get_tasks

st.set_page_config(
    page_title="Project Management Portal",
    page_icon="📋",
    layout="wide",
)

st.title("📋 Project Management Portal")

projects = get_projects()
tasks = get_tasks()

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
    project_id, name, description, status, created_date = project

    with st.container():
        st.markdown(f"### {name}")
        st.write(f"**Status:** {status}")
        st.write(f"**Description:** {description}")
        st.write(f"**Created Date:** {created_date}")
        st.divider()

st.subheader("Tasks")

for task in tasks:
    (
        task_id,
        project_id,
        task_name,
        description,
        priority,
        status,
        assigned_to,
        due_date,
        created_date,
    ) = task

    with st.container():
        st.markdown(f"### {task_name}")
        st.write(f"**Priority:** {priority}")
        st.write(f"**Status:** {status}")
        st.write(f"**Assigned To:** {assigned_to}")
        st.write(f"**Due Date:** {due_date}")
        st.write(f"**Description:** {description}")
        st.divider()