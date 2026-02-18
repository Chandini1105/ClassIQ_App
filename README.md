<<<<<<< HEAD
# ClassIQ - Classroom Allocation Management System

A comprehensive Django-based web application for managing classroom allocations, bookings, and scheduling in educational institutions.

## 📋 Table of Contents
=======
ClassIQ - Classroom Allocation Management System

A comprehensive Django-based web application for managing classroom allocations, bookings, and scheduling in educational institutions.

📋 Table of Contents
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Authentication](#authentication)
- [Database Models](#database-models)
- [Contributing](#contributing)
- [License](#license)

---
<<<<<<< HEAD

## ✨ Features

### Core Features
=======
✨ Features

Core Features
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
- **Classroom Allocation & Booking**: Easily allocate classrooms to faculty and courses
- **Real-time Availability**: Check classroom availability instantly
- **Conflict Detection**: Automatic detection of double-booking conflicts
- **User Management**: Web interface and command-line tools for user creation
- **Dashboard**: View ongoing and upcoming classroom allocations

<<<<<<< HEAD
### Authentication
=======
Authentication
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
- **Email-Based Login**: Use CMR email addresses (@cmr.edu.in) for authentication
- **Custom Authentication Backend**: Custom user authentication system
- **Default Password Management**: Automated password generation for new users
- **Role-Based Access**: Admin, Staff, and regular user roles

<<<<<<< HEAD
### Classroom Management
=======
Classroom Management
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
- **Room Tracking**: Manage classroom details (room number, capacity, status)
- **Active/Inactive Status**: Toggle classroom availability
- **Time Slot Management**: Configure school hours (default: 8:30 AM - 4:30 PM)
- **Capacity Planning**: Track classroom capacity for enrollment

<<<<<<< HEAD
### Faculty & Courses
=======
Faculty & Courses
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
- **Faculty Management**: Register and manage faculty members and their departments
- **Course Tracking**: Associate courses with faculty
- **Organizational Structure**: Organize by departments and academic years

---

<<<<<<< HEAD
## 🛠️ Tech Stack
=======
🛠️ Tech Stack
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738

- **Backend**: Django 5.2.10
- **Database**: SQLite (default), can be configured for PostgreSQL/MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Django's built-in auth system with custom backend
- **Python Version**: 3.8+

---

<<<<<<< HEAD
## 📁 Project Structure
=======
📁 Project Structure
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738

```
ClassIQ_App/
├── allocation/                  # Main Django app
│   ├── models.py               # Database models (Faculty, Course, Classroom, etc.)
│   ├── views.py                # View controllers and logic
│   ├── forms.py                # Form definitions
│   ├── urls.py                 # URL routing
│   ├── auth_backend.py         # Custom authentication backend
│   ├── admin.py                # Django admin configuration
│   ├── management/             # Custom management commands
│   │   └── commands/
│   │       └── add_user.py     # CLI user creation command
│   ├── templatetags/           # Custom template filters
│   │   └── custom_filters.py
│   └── migrations/             # Database migrations
├── classiq_project/            # Project settings
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   ├── asgi.py                 # ASGI configuration
│   └── wsgi.py                 # WSGI configuration
├── templates/                  # HTML templates
│   ├── base.html               # Base template
│   ├── login.html              # Login page
│   ├── dashboard.html          # Main dashboard
│   ├── book_classroom.html     # Classroom booking
│   ├── active_classes.html     # Active classes view
│   └── add_user.html           # User creation form
├── static/                     # Static files (CSS, JavaScript)
│   └── css/
│       └── style.css           # Main stylesheet
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django management script
├── AUTHENTICATION_GUIDE.md     # Detailed authentication setup guide
└── README.md                   # This file
```

---

<<<<<<< HEAD
## 🚀 Installation
=======
🚀 Installation
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

<<<<<<< HEAD
### Steps

1. **Clone the repository**
=======
Steps

1. Clone the repository**
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
   ```bash
   git clone https://github.com/Chandini1105/ClassIQ_App.git
   cd ClassIQ_App/classiq_project
   ```

<<<<<<< HEAD
2. **Create a virtual environment** (recommended)
=======
2. Create a virtual environment** (recommended)
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

<<<<<<< HEAD
3. **Install dependencies**
=======
3. Install dependencies**
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
   ```bash
   pip install django==5.2.10
   ```

<<<<<<< HEAD
4. **Apply database migrations**
=======
4. Apply database migrations**
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
   ```bash
   python manage.py migrate
   ```

<<<<<<< HEAD
5. **Create a superuser (admin account)**
=======
5. Create a superuser (admin account)**
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
   ```bash
   python manage.py createsuperuser
   ```

<<<<<<< HEAD
6. **Run the development server**
=======
6. Run the development server**
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
   ```bash
   python manage.py runserver
   ```

<<<<<<< HEAD
7. **Access the application**
=======
7. Access the application**
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
   - Open your browser and navigate to: `http://127.0.0.1:8000`

---

<<<<<<< HEAD
## ⚙️ Configuration

### Settings File
=======
⚙️ Configuration

Settings File
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
Edit `classiq_project/settings.py` to configure:

- **DEBUG**: Set to `False` for production
- **ALLOWED_HOSTS**: Add your domain names
- **DATABASES**: Configure your database (default is SQLite)
- **SECRET_KEY**: Generate a new secret key for production

<<<<<<< HEAD
### Environment Variables (Recommended)
=======
Environment Variables (Recommended)
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
Create a `.env` file in the project root:
```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
```

<<<<<<< HEAD
### Time Configuration
=======
Time Configuration
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
Modify school hours in `allocation/models.py`:
```python
SCHOOL_START_TIME = time(8, 30)   # 8:30 AM
SCHOOL_END_TIME = time(16, 30)    # 4:30 PM
```

---

<<<<<<< HEAD
## 📖 Usage

### Dashboard
=======
📖 Usage

Dashboard
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
After logging in, you'll see a dashboard with:
- **Ongoing Classes**: Currently active classroom allocations
- **Upcoming Classes**: Classes scheduled for later today
- **Busy Rooms**: Rooms currently in use
- **Available Classrooms**: Free classrooms ready for booking

<<<<<<< HEAD
### Book a Classroom
=======
Book a Classroom
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
1. Navigate to the classroom booking page
2. Select desired date, start time, and duration
3. Choose the faculty and course
4. Select an available classroom
5. Confirm the allocation

<<<<<<< HEAD
### View Active Classes
- Check the "Active Classes" page to see all current allocations
- Filter by date, faculty, or classroom as needed

### Admin Panel
=======
View Active Classes
- Check the "Active Classes" page to see all current allocations
- Filter by date, faculty, or classroom as needed

Admin Panel
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
- Access Django admin at `/admin/`
- Manage users, classrooms, faculty, and courses
- View and edit allocations
- Generate reports

---

<<<<<<< HEAD
## 🔐 Authentication

### Email-Based Login
- **Username**: Use your CMR email (e.g., `john.doe@cmr.edu.in`)
- **Password**: Default is `CMRU 1` (please change after first login)

### User Management

#### Method 1: Web Interface
=======
🔐 Authentication

Email-Based Login
- **Username**: Use your CMR email (e.g., `john.doe@cmr.edu.in`)
- **Password**: Default is `CMRU 1` (please change after first login)

User Management

Method 1: Web Interface
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
1. Login as admin/staff
2. Navigate to `/admin/add-user/`
3. Enter full name and email
4. Click "Create User"

<<<<<<< HEAD
#### Method 2: Command Line
=======
Method 2: Command Line
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
```bash
python manage.py add_user "John Doe" --email johndoe@cmr.edu.in
```

<<<<<<< HEAD
### Custom Authentication
=======
Custom Authentication
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
The application uses a custom email-based authentication backend:
- Located in `allocation/auth_backend.py`
- Validates users by email instead of username
- Ensures unique email addresses across the system

For detailed authentication setup, see [AUTHENTICATION_GUIDE.md](./AUTHENTICATION_GUIDE.md).

---

<<<<<<< HEAD
## 🗄️ Database Models

### Faculty
- `name`: Faculty member's full name
- `department`: Department name

### Course
=======
🗄️ Database Models

Faculty
- `name`: Faculty member's full name
- `department`: Department name

Course
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
- `name`: Course name
- `year`: Academic year
- `faculty`: Foreign key to Faculty

<<<<<<< HEAD
### Classroom
=======
Classroom
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
- `room_number`: Unique room identifier
- `capacity`: Maximum student capacity
- `is_active`: Active/inactive status

<<<<<<< HEAD
### Allocation
=======
Allocation
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
- `classroom`: Booked classroom
- `course`: Course being taught
- `date`: Allocation date
- `start_time`: Start time of class
- `duration_minutes`: Duration of allocation
- `student_leader`: Student in charge

<<<<<<< HEAD
### StudentLeader
=======
StudentLeader
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
- `name`: Student's name
- `email`: Contact email
- `course`: Associated course

---

<<<<<<< HEAD
## 🤝 Contributing
=======
🤝 Contributing
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

<<<<<<< HEAD
### Coding Guidelines
=======
Coding Guidelines
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test your changes before submitting

---

<<<<<<< HEAD
## 🐛 Troubleshooting

### Database Issues
=======
🐛 Troubleshooting

Database Issues
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
```bash
# Reset database (WARNING: deletes all data)
rm db.sqlite3
python manage.py migrate
```

<<<<<<< HEAD
### Migration Errors
=======
Migration Errors
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
```bash
# Create and run migrations
python manage.py makemigrations
python manage.py migrate
```

<<<<<<< HEAD
### Static Files Not Loading
=======
Static Files Not Loading
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
```bash
# Collect static files
python manage.py collectstatic
```

<<<<<<< HEAD
### Login Issues
- Ensure you have created a user: `python manage.py add_user "Your Name" --email your.email@cmr.edu.in`
- Default password is `CMRU 1`
=======
Login Issues
- Ensure you have created a user: `python manage.py add_user "Your Name" --email your.email@cmr.edu.in`
- Default password is `******`
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738
- Check that email format includes `@cmr.edu.in`

---

<<<<<<< HEAD
## 📝 License
=======
📝 License
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738

This project is licensed under the MIT License - see the LICENSE file for details.

---

<<<<<<< HEAD
## 👨‍💻 Author
=======
👨‍💻 Author
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738

**Chandini** - [GitHub Profile](https://github.com/Chandini1105)

---

<<<<<<< HEAD
## 📞 Support
=======
📞 Support
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738

For issues, questions, or suggestions, please:
- Open an issue on GitHub
- Check the [AUTHENTICATION_GUIDE.md](./AUTHENTICATION_GUIDE.md) for authentication-related questions
- Review existing issues for solutions

---

<<<<<<< HEAD
## 🎯 Future Enhancements
=======
🎯 Future Enhancements
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738

- [ ] Email notifications for classroom allocations
- [ ] Bulk import of users and allocations
- [ ] Student enrollment management
- [ ] Classroom usage analytics and reporting
- [ ] API endpoints for mobile integration
- [ ] Calendar view for schedule visualization
- [ ] Multi-day allocation support
- [ ] Conflict resolution workflow

---

<<<<<<< HEAD
**Last Updated**: February 2026
=======
>>>>>>> 2f9e5273232b0935dcde3fe8037b519e0ee27738

## Deployment Notes
For cloud deploys, use a managed Postgres database and set `DATABASE_URL`.
SQLite is not suitable for cloud deployments.
Example: `postgres://user:pass@host:port/dbname`

