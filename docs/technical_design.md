# Technical Design Document

## Solution Overview

The Project Management Portal is a Python-based application that demonstrates project and task management workflows through a FastAPI backend, SQLite database, service layer architecture, and Streamlit dashboard interface.

## Technology Stack

- Python
- FastAPI
- Streamlit
- SQLite
- Git
- GitHub

## Solution Components

### API Layer

Located in:

```text
src/api/main.py
```
Responsible for exposing project and task functionality through FastAPI.

### Dashboard Layer

Located in:

```text
src/dashboard/project_viewer.py
```
Provides a Streamlit interface for viewing and managing project-related data.

### Database Layer

Located in:

```text
src/database/create_database.py
```
Creates and manages the SQLite database structure.

### Service Layer

Located in:

```text
src/services/
```
Responsible for project and task business logic.

### Project Service

Located in:

```text
src/services/task_service.py/
```
Handles task-related operations.

## Data Flow

```text
User
↓
Streamlit Dashboard / FastAPI API
↓
Project & Task Services
↓
SQLite Database
↓
Project / Task Records
```



