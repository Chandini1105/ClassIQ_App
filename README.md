# ClassIQ - Classroom Allocation Management System

ClassIQ is a Django-based web application for managing classroom bookings, daily schedules, and room availability in an academic environment.

## Features

- Classroom booking with conflict detection.
- Live dashboard for ongoing and upcoming classes.
- Room availability status by current time.
- Email-based authentication using a custom backend.
- Admin/staff user creation from UI and management command.
- Optional default-user/bootstrap behavior for cloud deployment.

## Tech Stack

- Python 3.11+
- Django 5.2.10
- SQLite (local default) or PostgreSQL/MySQL via `DATABASE_URL`
- WhiteNoise for static file serving

## Project Structure

```text
classiq_project/
|-- allocation/
|   |-- management/commands/
|   |   |-- add_user.py
|   |   `-- ensure_default_user.py
|   |-- migrations/
|   |-- templatetags/custom_filters.py
|   |-- utils/default_user.py
|   |-- admin.py
|   |-- auth_backend.py
|   |-- forms.py
|   |-- models.py
|   |-- urls.py
|   `-- views.py
|-- classiq_project/
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- static/css/style.css
|-- static/images/logo.svg
|-- templates/
|   |-- active_classes.html
|   |-- add_user.html
|   |-- base.html
|   |-- book_classroom.html
|   |-- dashboard.html
|   |-- help.html
|   `-- login.html
|-- AUTHENTICATION_GUIDE.md
|-- manage.py
|-- requirements.txt
`-- test_timezone.py
```

## URL Routes

- `/` -> Dashboard
- `/login/` -> Login page
- `/logout/` -> Logout
- `/book/` -> Classroom booking
- `/active-classes/` -> Daily class status
- `/help/` -> Help page
- `/admin/add-user/` -> Staff-only user creation
- `/admin/` -> Django admin

## Data Model

- `Faculty`: name, department.
- `Course`: name, year, faculty.
- `Classroom`: room number, capacity, active flag.
- `StudentLeader`: name.
- `Allocation`: student leader, course, classroom, date, start time, duration.

`Allocation` records are used to compute ongoing/upcoming/completed status and detect booking overlaps.

## Setup (Local)

1. Clone and enter the project:
   ```bash
   git clone https://github.com/Chandini1105/ClassIQ_App.git
   cd ClassIQ_App/classiq_project
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create admin user:
   ```bash
   python manage.py createsuperuser
   ```
6. Run server:
   ```bash
   python manage.py runserver
   ```

## Environment Configuration

Primary settings are in `classiq_project/settings.py`.

Common environment variables:

- `DEBUG` (`True`/`False`)
- `SECRET_KEY`
- `ALLOWED_HOSTS` (comma-separated)
- `CSRF_TRUSTED_ORIGINS` (comma-separated, full `https://...`)
- `DATABASE_URL`

Optional auth/bootstrap variables:

- `DEFAULT_LOGIN_EMAIL`
- `DEFAULT_LOGIN_PASSWORD`
- `DEFAULT_LOGIN_NAME`
- `DEFAULT_LOGIN_RESET_PASSWORD`
- `DEFAULT_LOGIN_IS_STAFF`
- `DEFAULT_LOGIN_IS_SUPERUSER`
- `AUTO_PROVISION_USERS`

## User Management

- Web UI (staff only): `/admin/add-user/`
- CLI command:
  ```bash
  python manage.py add_user "John Doe" --email johndoe@cmr.edu.in
  ```
- Default password in current code: `CMRU 1`

## Notes

- School hours are currently defined in `allocation/models.py` as `08:30` to `16:30`.
- Default classroom seeds are defined in `allocation/views.py` and ensured during dashboard/booking flows.
