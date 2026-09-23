# Company Leave Management System

A backend-focused **Leave Management System** built with **Flask**, demonstrating RESTful API development, JWT authentication, role-based authorization, database operations, and a structured employee leave approval workflow.

## Overview

The system provides separate functionalities for **Admin, Manager, and Employee** roles. It implements secure authentication and authorization while managing employee records and leave requests through RESTful APIs.

The leave workflow follows:

**Employee → Submit Leave Request → Manager → Approve / Reject**

## Features

### Admin

* Admin signup and login
* Create Manager accounts
* Create Employee accounts
* View registered users
* Role-based access control

### Manager

* Secure login
* View employees assigned to their team
* View team members' leave requests
* Approve or reject leave requests
* Track leave status of team members

### Employee

* Secure login
* Submit leave requests
* View personal leave requests
* Track approval/rejection status

## Technical Highlights

* RESTful API architecture
* JWT-based authentication
* Role-Based Access Control (RBAC)
* Custom middleware/decorators for authorization
* SQLAlchemy ORM for database operations
* Structured Flask application architecture
* Employee-to-manager relationship management
* Leave request approval workflow
* Basic automated API testing
* Postman collection for API testing

## Tech Stack

| Category         | Technology               |
| ---------------- | ------------------------ |
| Backend          | Flask                    |
| Database         | SQLite                   |
| ORM              | SQLAlchemy               |
| Authentication   | JWT                      |
| API Architecture | RESTful APIs             |
| Testing          | Python / Automated Tests |
| API Testing      | Postman                  |

> The database configuration can be extended to support PostgreSQL or MySQL.

## Project Structure

```text
leave_manage/
│
├── routes/
│   ├── auth_routes.py       # Signup and login APIs
│   ├── leave_routes.py      # Leave request and approval APIs
│   └── user_routes.py       # User creation and management APIs
│
├── tests/
│   └── test_basic.py        # Basic automated tests
│
├── utils/
│   └── decorators.py        # JWT and role-based access decorators
│
├── app.py                   # Application entry point
├── config.py                # Application configuration
├── models.py                # Database models
├── postman_collection.json  # Postman API collection
└── requirements.txt         # Project dependencies
```

## API Endpoints

| Method | Endpoint              | Access   | Description                           |
| ------ | --------------------- | -------- | ------------------------------------- |
| POST   | `/auth/signup`        | Public   | Register an Admin                     |
| POST   | `/auth/login`         | Public   | Login for Admin, Manager, or Employee |
| POST   | `/users/manager`      | Admin    | Create a Manager                      |
| POST   | `/users/employee`     | Admin    | Create an Employee                    |
| GET    | `/users/employees`    | Manager  | Get employees assigned to the Manager |
| POST   | `/leave/request`      | Employee | Submit a leave request                |
| GET    | `/leave/requests`     | Manager  | View team leave requests              |
| PATCH  | `/leave/request/<id>` | Manager  | Approve or reject a leave request     |
| GET    | `/leave/my-requests`  | Employee | View personal leave requests          |

## Authentication & Authorization

The application uses **JSON Web Tokens (JWT)** to authenticate users.

After successful login, the generated token is used to access protected endpoints.

Role-based authorization ensures that users can access only the resources and operations permitted for their role.

### Access Levels

```text
Admin
 ├── Create Managers
 ├── Create Employees
 └── View Users

Manager
 ├── View Team
 ├── View Leave Requests
 └── Approve / Reject Leave

Employee
 ├── Submit Leave Request
 └── View Own Leave Requests
```

## Leave Approval Workflow

```text
Employee
    │
    ▼
Submit Leave Request
    │
    ▼
Manager Reviews Request
    │
    ├── Approve
    │
    └── Reject
    │
    ▼
Employee Views Updated Status
```

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd leave_manage
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

The Flask application will start on the configured local server.

## API Testing

The project includes a `postman_collection.json` file containing the API requests required to test the application's functionality.

You can import the collection into **Postman** and test:

* Authentication
* User management
* Employee management
* Leave requests
* Leave approval/rejection
* Role-based access

## Learning Outcomes

This project demonstrates practical understanding of:

* Flask backend development
* REST API design
* JWT authentication
* Role-based authorization
* SQLAlchemy and relational database operations
* Middleware and custom decorators
* API testing
* Backend application structure
* Authentication and access-control workflows

## Future Improvements

Potential improvements include:

* PostgreSQL/MySQL production database support
* Refresh token implementation
* Email notifications for leave approvals
* Admin dashboard
* Pagination and filtering
* Docker deployment
* API documentation using Swagger/OpenAPI
* Production deployment with cloud infrastructure

---
## Author

**Kalpesh Nivilkar**
B.E. Artificial Intelligence & Data Science
Pune, Maharashtra, India

* GitHub: `github.com/KalpeshNivilkar`
* LinkedIn: `linkedin.com/kalpeshnivilkar`


### Project Focus

**Flask • REST APIs • JWT Authentication • Role-Based Authorization • SQLAlchemy • SQLite • Backend Development**
