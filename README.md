# SIWES / Industrial Training Placement Management System (Backend)

A role-based backend system for managing **student industrial training (SIWES/IT)** placements, logbooks, attendance, supervision, mentorship, and institutional verification.

Built with **Django + Django REST Framework**.

---

## Core Roles

- Student
- Institution Admin
- Institution Supervisor
- Company Mentor
- System Admin

Each role has **strict permissions and dedicated workflows**.

---

## Authentication (JWT)

### 1. Register

`POST /api/users/register/`

**Request Body Types(JSON)**

```typescript
{
  "email_address": string;  // e.g"student@example.com"
  "password": string; // e.g"StroHs53e^tqe762"
  "role": "student" | "supervisor" | "institution" | "mentor";
  "first_name": string; //e.g "John"
  "last_name": string; //e.g "Doe"
  "other_names"?: string;
}
```

**Successful Request Sample**

```json
{
  "id": "ff190240-de71-473b-a381-2111f0b9713c",
  "email_address": "falade@gmail.com",
  "first_name": "Folasade",
  "other_names": "Tolulope",
  "last_name": "Fashina",
  "role": "supervisor"
}
```

### 2. Login

`POST /api/users/login/`

**Request Body Types(JSON)**

```typescript
{
  "email_address": string;
  "password": string;
}
```

**Successful Request Sample**

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2OTE4OTAwMCwiaWF0IjoxNzY4NTg0MjAwLCJqdGkiOiIxYmQ2NjcyOGNjNGI0OWFjYWU4NGYwYzg5NzY5MzRkMSIsInVzZXJfaWQiOiJmZjE5MDI0MC1kZTcxLTQ3M2ItYTM4MS0yMTExZjBiOTcxM2MifQ.bgILfbe_jYaYbOWdTixENObQYiSqxJrZLwZBvb41a8Y",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY4NTkxNDAwLCJpYXQiOjE3Njg1ODQyMDAsImp0aSI6IjZiN2JjNjYzYzc0YjQzZDdhZjBhN2E5ZTU4NzRkZjIwIiwidXNlcl9pZCI6ImZmMTkwMjQwLWRlNzEtNDczYi1hMzgxLTIxMTFmMGI5NzEzYyJ9.zHNg5on22fIrATLmWsyLBN5A0twnzOGLp7LGVjVot6M",
  "user": {
    "id": "ff190240-de71-473b-a381-2111f0b9713c",
    "email_address": "falade@gmail.com"
  }
}
```

The access token is used to access protected route and expires after 2 hours. The refresh token is used to get a new access token and expires after 7 days.

### **3. Refresh Token**

`POST /api/users/refresh_token/`

**Request Body Types(JSON)**

```typescript
{
  refresh: string;
}
```

**Successful Response**

```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY4NTkxNzQ0LCJpYXQiOjE3Njg1ODQ1NDQsImp0aSI6IjNjOWZjNGUxYzMxZDRkOTM5YTI2YWVhOTVmOWEwMGEwIiwidXNlcl9pZCI6ImZmMTkwMjQwLWRlNzEtNDczYi1hMzgxLTIxMTFmMGI5NzEzYyJ9.O3Ptra0iowr1RSJ2rqmCHdSFbFualjffEunViE2H_oI"
}
```

## Profile Creation (After Registration)

To access all routes, include the JWT token in the **Authorization** header as follows:

```json
{
  "Authorization": "Bearer <access-token>"
}
```

### 1.Student Institution Profile

`POST /students/institution_profile/`
**Request Body Types(JSON)**

```typescript
{
  "matric_number": string;
  "department": string;
  "level": string;
  "institution_id" string;
  "faculty"?: string;
  "programme": "B.Sc" | "B.Ed" | "BA" | "ND"
}
```

**Successful Response**

```json
{
  "id": "53707ba7-4642-4a2d-a10c-85e7d77a06b3",
  "matric_no": "230408033",
  "department": "Mathematics",
  "faculty": "PELSSA",
  "programme": "B.Sc",
  "level": "300",
  "status": "pending",
  "user": "6c42431f-00b4-4c45-9359-1eb52e9cb363",
  "institution": "9bac85cb-36d5-4f28-8f19-bceffc518c16"
}
```
