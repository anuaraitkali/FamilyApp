# Architecture Design

## 1. System Design
- The system uses microservices for scaling backend features independently.



## 2. Key Components and Responsibilities

### 2.1 Frontend (React Web App)
- **Responsibilities**:
  - Provide a user-friendly UI for accessing all features (calendar, finances, messaging, etc.).
  - Communicate with backend APIs via RESTful endpoints or GraphQL.
- **Tech Stack**: React + Material UI for design consistency.

### 2.2 Mobile App (React Native)
- **Responsibilities**:
  - Provide seamless access across devices for on-the-go usage.
  - Feature parity with the web app (except heavy administrative tasks).

### 2.3 API Gateway
- **Purpose**:
  - Centralized entry point for routing requests to backend services.
  - Handles authentication, rate limiting, and load balancing.
- **Tech**: Azure API Management or NGINX as Ingress in Kubernetes.

### 2.4 Backend Services (Microservices)
- Built in Django, with services communicating via REST APIs.
- **Core Services**:
  - **User Management**: Handles user authentication, roles, and profiles.
  - **Group Management**: Manages family groups and permissions.
  - **Financial Management**: Handles budgeting, expense tracking, and future bill reminders.
  - **Calendar**: Provides CRUD for events and scheduling.
  - **Messaging**: Real-time communication between users (family members).
  - **Media Storage**: Handles uploads and organization of family photos, videos, and documents.

## 3. Database Layer
- **PostgreSQL**: Relational database for structured data (users, events, finances).
- **Azure Blob Storage**: For unstructured media data (photos, videos, documents).
- **Redis Cache**: For caching frequently accessed data like user sessions and calendar events.

## 4. Example Data Schema

- **Users Table**:
  - user_id, name, email, password_hash, role, profile_picture.

- **Families Table**:
  - family_id, owner_id, family_name.

- **Expenses Table**:
  - expense_id, family_id, amount, category, timestamp.

- **Media Files**:
  - Stored in Blob Storage, metadata tracked in SQL Server (file_id, file_url, uploaded_by).

## 5. DevOps and Cloud Infrastructure

### 5.1 Core Infrastructure
- **Azure VM with Kubernetes (K8)**:
  - Orchestrates microservices, ensuring high availability and scalability.
- **Docker Containers**:
  - Containerize each service for portability and isolation.

### 5.2 CI/CD Pipelines
- **GitHub Actions**:
  - Automate code testing, building, and deployments to Kubernetes.
- **Terraform**:
  - Infrastructure as Code (IaC) for consistent cloud resource provisioning.

### 5.3 Monitoring & Logging
- **Prometheus + Grafana**:
  - Monitor metrics (CPU, memory, uptime).
- **Azure Monitor + ELK Stack**:
  - Centralized logging for error detection and debugging.
