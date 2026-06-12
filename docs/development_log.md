# Development Log

## Issue #1 — Create Project Management Database Schema

### Status
Completed

### Summary
Implemented the initial SQLite database schema for the Project Management Portal.

### Work Completed
- Created `projects` table
- Created `tasks` table
- Added primary keys
- Added foreign key relationship between tasks and projects
- Created reusable database initialization script
- Verified database structure in DBeaver

### Files Added
- `src/database/create_database.py`

---

## Issue #2 — Create Project CRUD Operations

### Status
Completed

### Summary
Implemented project-level CRUD operations for the Project Management Portal.

### Work Completed
- Added `create_project()` function
- Added `get_projects()` function
- Added `update_project()` function
- Added `delete_project()` function
- Inserted sample project records
- Verified project records in DBeaver
- Confirmed create, read, update, and delete behavior

### Files Added
- `src/services/project_service.py`