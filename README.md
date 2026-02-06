# ClassIQ - Classroom Allocation Management System

A comprehensive Django-based web application for managing classroom allocations, bookings, and scheduling in educational institutions.

## 📋 Table of Contents

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

## ✨ Features

### Core Features
- **Classroom Allocation & Booking**: Easily allocate classrooms to faculty and courses
- **Real-time Availability**: Check classroom availability instantly
- **Conflict Detection**: Automatic detection of double-booking conflicts
- **User Management**: Web interface and command-line tools for user creation
- **Dashboard**: View ongoing and upcoming classroom allocations

### Authentication
- **Email-Based Login**: Use CMR email addresses (@cmr.edu.in) for authentication
- **Custom Authentication Backend**: Custom user authentication system
- **Default Password Management**: Automated password generation for new users
- **Role-Based Access**: Admin, Staff, and regular user roles

### Classroom Management
- **Room Tracking**: Manage classroom details (room number, capacity, status)
- **Active/Inactive Status**: Toggle classroom availability
- **Time Slot Management**: Configure school hours (default: 8:30 AM - 4:30 PM)
- **Capacity Planning**: Track classroom capacity for enrollment

### Faculty & Courses
- **Faculty Management**: Register and manage faculty members and their departments
- **Course Tracking**: Associate courses with faculty
- **Organizational Structure**: Organize by departments and academic years

---

## 🛠️ Tech Stack

- **Backend**: Django 5.2.10
- **Database**: SQLite (default), can be configured for PostgreSQL/MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Django's built-in auth system with custom backend
- **Python Version**: 3.8+

---

## 📁 Project Structure

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

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Chandini1105/ClassIQ_App.git
   cd ClassIQ_App/classiq_project
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django==5.2.10
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:8000`

---

## ⚙️ Configuration

### Settings File
Edit `classiq_project/settings.py` to configure:

- **DEBUG**: Set to `False` for production
- **ALLOWED_HOSTS**: Add your domain names
- **DATABASES**: Configure your database (default is SQLite)
- **SECRET_KEY**: Generate a new secret key for production

### Environment Variables (Recommended)
Create a `.env` file in the project root:
```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
```

### Time Configuration
Modify school hours in `allocation/models.py`:
```python
SCHOOL_START_TIME = time(8, 30)   # 8:30 AM
SCHOOL_END_TIME = time(16, 30)    # 4:30 PM
```

---

## 📖 Usage

### Dashboard
After logging in, you'll see a dashboard with:
- **Ongoing Classes**: Currently active classroom allocations
- **Upcoming Classes**: Classes scheduled for later today
- **Busy Rooms**: Rooms currently in use
- **Available Classrooms**: Free classrooms ready for booking

### Book a Classroom
1. Navigate to the classroom booking page
2. Select desired date, start time, and duration
3. Choose the faculty and course
4. Select an available classroom
5. Confirm the allocation

### View Active Classes
- Check the "Active Classes" page to see all current allocations
- Filter by date, faculty, or classroom as needed

### Admin Panel
- Access Django admin at `/admin/`
- Manage users, classrooms, faculty, and courses
- View and edit allocations
- Generate reports

---

## 🔐 Authentication

### Email-Based Login
- **Username**: Use your CMR email (e.g., `john.doe@cmr.edu.in`)
- **Password**: Default is `CMRU 1` (please change after first login)

### User Management

#### Method 1: Web Interface
1. Login as admin/staff
2. Navigate to `/admin/add-user/`
3. Enter full name and email
4. Click "Create User"

#### Method 2: Command Line
```bash
python manage.py add_user "John Doe" --email johndoe@cmr.edu.in
```

### Custom Authentication
The application uses a custom email-based authentication backend:
- Located in `allocation/auth_backend.py`
- Validates users by email instead of username
- Ensures unique email addresses across the system

For detailed authentication setup, see [AUTHENTICATION_GUIDE.md](./AUTHENTICATION_GUIDE.md).

---

## 🗄️ Database Models

### Faculty
- `name`: Faculty member's full name
- `department`: Department name

### Course
- `name`: Course name
- `year`: Academic year
- `faculty`: Foreign key to Faculty

### Classroom
- `room_number`: Unique room identifier
- `capacity`: Maximum student capacity
- `is_active`: Active/inactive status

### Allocation
- `classroom`: Booked classroom
- `course`: Course being taught
- `date`: Allocation date
- `start_time`: Start time of class
- `duration_minutes`: Duration of allocation
- `student_leader`: Student in charge

### StudentLeader
- `name`: Student's name
- `email`: Contact email
- `course`: Associated course

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Coding Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test your changes before submitting

---

## 🐛 Troubleshooting

### Database Issues
```bash
# Reset database (WARNING: deletes all data)
rm db.sqlite3
python manage.py migrate
```

### Migration Errors
```bash
# Create and run migrations
python manage.py makemigrations
python manage.py migrate
```

### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic
```

### Login Issues
- Ensure you have created a user: `python manage.py add_user "Your Name" --email your.email@cmr.edu.in`
- Default password is `CMRU 1`
- Check that email format includes `@cmr.edu.in`

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Chandini** - [GitHub Profile](https://github.com/Chandini1105)

---

## 📞 Support

For issues, questions, or suggestions, please:
- Open an issue on GitHub
- Check the [AUTHENTICATION_GUIDE.md](./AUTHENTICATION_GUIDE.md) for authentication-related questions
- Review existing issues for solutions

---

## 🎯 Future Enhancements

- [ ] Email notifications for classroom allocations
- [ ] Bulk import of users and allocations
- [ ] Student enrollment management
- [ ] Classroom usage analytics and reporting
- [ ] API endpoints for mobile integration
- [ ] Calendar view for schedule visualization
- [ ] Multi-day allocation support
- [ ] Conflict resolution workflow

---

**Last Updated**: February 2026
