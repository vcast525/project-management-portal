import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.services.project_service import get_projects

st.set_page_config(
    page_title="Project Management Portal",
    page_icon="📋",
    layout="wide",
)

st.title("📋 Project Management Portal")

projects = get_projects()

st.metric(
    label="Total Projects",
    value=len(projects)
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