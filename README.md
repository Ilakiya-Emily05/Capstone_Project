Digital Banking and Loan Management API

Overview
This project is a RESTful API for a Digital Banking System built using FastAPI. The system supports core banking operations such as account creation, money transfers, loan applications, approvals, and administrative reporting. The application is designed with clean architecture principles, role-based access control, and scalable deployment in mind.

The system supports three primary roles:
Customer: Can register, create accounts, transfer money, and apply for loans.
Bank Officer: Can review and approve or reject loan applications.
Admin: Can monitor system activity, manage accounts, and generate reports.

Technology Stack
Backend Framework: FastAPI
ORM: SQLAlchemy
Database: PostgreSQL
Authentication: JWT based authentication
Containerization: Docker and Docker Compose
Caching and Concurrency Control: Redis
Testing: Pytest

Project Structure
The project follows a layered architecture separating concerns clearly across modules.

app
Contains the core application logic.

main.py
Application entry point. Initializes FastAPI app, middleware, and routes.

core
Holds configuration and infrastructure-related code including environment settings, database connection, security utilities, and dependency injection.

models
Contains SQLAlchemy ORM models such as User, Account, Transaction, and Loan.

schemas
Contains Pydantic schemas used for request validation and response serialization.

repositories
Implements the data access layer responsible for database operations.

services
Contains business logic for authentication, users, accounts, transactions, and loans.

api
Defines API routes and includes routers for different modules such as auth, accounts, transactions, and loans.

middleware
Includes cross-cutting concerns such as CORS handling, logging, and rate limiting.

exceptions
Centralized custom exception definitions and global exception handlers.

utils
Helper utilities including validators and constants.

alembic
Manages database migrations.

tests
Contains unit tests and integration tests for major workflows.

Dockerfile and docker-compose.yml
Used for containerized deployment of the application and its dependencies.

requirements.txt
Lists all Python dependencies required for the project.

Authentication
The application uses JWT for authentication and authorization.
Upon successful login, users receive a token which must be included in subsequent requests to access protected endpoints.
Role-based access control is enforced for Customer, Officer, and Admin operations.

Database Design
Users table stores user credentials and roles.
Accounts table stores bank account details and balances.
Transactions table records all money movements between accounts.
Loans table stores loan applications and their approval status.

Sprint Breakdown

Sprint 1
User registration and login
Account creation
Money transfer between accounts
View account details
Basic integration tests

Sprint 2
Loan application workflow
Loan approval and rejection by officers
Admin reports and monitoring
Additional account and user management APIs

Sprint 3
Microservice-based architecture
Separate services for authentication, accounts, transactions, loans, and reporting
Inter-service communication using REST
Redis for locking and caching
Container orchestration using Docker Compose

End-to-End Workflow
A customer registers and logs in.
The customer creates a bank account.
The customer performs money transfers or applies for a loan.
A bank officer reviews and approves or rejects the loan.
The admin monitors transactions and generates reports.

Deployment
The application is designed to be deployed using Docker and Docker Compose.
PostgreSQL and Redis are configured as supporting services.

