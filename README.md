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

### Register

`POST /api/users/register/`

**Sample Body**

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
