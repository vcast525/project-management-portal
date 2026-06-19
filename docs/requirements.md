# Requirements Document

## Project Name

Project Management Portal

## Business Problem

Organizations need structured tools to manage projects, tasks, ownership, due dates, and delivery status. Without centralized project tracking, teams may rely on spreadsheets, email updates, and manual status reporting, which can create delays, inconsistent visibility, and poor accountability.

## Business Objective

Develop a project management portal that allows users to create projects, create tasks, track project status, manage task ownership, and view project delivery information through a dashboard and API.

## Functional Requirements

- Create project records
- Create task records
- Store project and task data in SQLite
- View project records through a dashboard
- View task records through a dashboard
- Expose project and task functionality through FastAPI
- Support project service logic
- Support task service logic
- Provide project and task screenshots
- Document development progress

## Non-Functional Requirements

- Modular code structure
- Maintainable service layer
- Local database persistence
- Lightweight dashboard interface
- API-based application structure
- Clear separation of concerns
- Portfolio-ready documentation

## Success Criteria

- Projects can be created successfully
- Tasks can be created successfully
- Project and task records persist in SQLite
- Dashboard displays project management data
- Swagger UI exposes API functionality
- Project structure is clean and maintainable