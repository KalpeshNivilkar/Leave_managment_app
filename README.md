# 🏢 Company Leave Management System (Flask + JWT )

A **miniature** Leave Management System built with **Flask** demonstrating:

- ✅ RESTful API Design  
- 🔐 JWT Authentication  
- 👤 Role-Based Authorization (Admin, Manager, Employee)  
- 🛠 Middleware for Access Control  
- 🗄 Database Operations with SQLAlchemy  
- 📄 Leave Approval Flow (Employee → Manager)

---

## 📌 Features

### **1️⃣ Admin**
- Signup/Login
- Add Manager
- Add Employee
- View all users

### **2️⃣ Manager**
- Login
- View their team (Employees)
- Approve / Reject Leave Requests
- View leave status of team members

### **3️⃣ Employee**
- Login
- Submit Leave Request
- View their own Leave Requests & Status

---

## 🛠 Tech Stack

- **Backend Framework**: Flask
- **Database**: SQLite (easily switchable to PostgreSQL/MySQL)
- **Auth**: JWT (JSON Web Token)
- **ORM**: SQLAlchemy

---

## 📂 Project Structure
leave_manage/
├── routes/
│  ├── auth_routes.py # Signup/Login APIs
│  ├── leave_routes.py # Leave request & approval APIs
│  ├── user_routes.py # User creation & management APIs
├── tests/
│  └── test_basic.py # Basic automated tests
├── utils/
│  └── decorators.py # JWT & role-based access decorators
├── app.py # Application entry point
├── config.py # App configuration
├── models.py # Database models
├── postman_collection.json # Postman collection for API testing
├── requirements.txt # Dependencies

## 🔑 API Endpoints

| Method | Endpoint            | Access   | Description                    |
| ------ | ------------------- | -------- | ------------------------------ |
| POST   | /auth/signup        | Public   | Admin Signup                   |
| POST   | /auth/login         | Public   | Login (Admin/Manager/Employee) |
| POST   | /users/manager      | Admin    | Create Manager                 |
| POST   | /users/employee     | Admin    | Create Employee                |
| GET    | /users/employees    | Manager  | Get Employees under Manager    |
| POST   | /leave/request      | Employee | Submit Leave Request           |
| GET    | /leave/requests     | Manager  | View Leave Requests of Team    |
| PATCH  | /leave/request/<id> | Manager  | Approve / Reject Leave         |
| GET    | /leave/my-requests  | Employee | View Own Leave Requests        |


