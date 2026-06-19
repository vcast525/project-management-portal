# Architecture Document

## Architecture Overview

The Project Management Portal uses a layered architecture that separates API routing, dashboard presentation, service logic, and database persistence.

## High-Level Architecture

```text
User
↓
Streamlit Dashboard
↓
Project / Task Service Layer
↓
SQLite Database
```

## API Architecture

```text
API Consumer
↓
FastAPI Endpoints
↓
Project Service / Task Service
↓
SQLite Database
```

## Folder Structure

```text
project-management-portal/
├── data/
│   └── project_management_portal.db
├── docs/
│   ├── images/
│   └── development_log.md
├── src/
│   ├── api/
│   ├── dashboard/
│   ├── database/
│   ├── models/
│   └── services/
├── tests/
└── README.md
```
## Design Principles
* Separation of concerns
* Secure password handling
* Token-based authentication
* Role-based authorization
* Database-backed access control
* Test-driven validation
* Portfolio-ready architecture