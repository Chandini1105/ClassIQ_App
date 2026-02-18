# ClassIQ - Custom Authentication Setup Guide

## Overview
The authentication system has been updated to:
- Use **@cmr.edu.in email addresses** as usernames
- Set **"CMRU 1"** as the default password for all new users
- Support easy user creation via web interface or command line

---

## ✨ Features Implemented

### 1. **Email-Based Authentication**
- Users login with their email address (e.g., `john.doe@cmr.edu.in`)
- Custom backend (`EmailBackend`) in `allocation/auth_backend.py`
- Unique emails prevent duplicate accounts

### 2. **Web Interface for User Management**
- **URL**: `/admin/add-user/`
- **Access**: Staff/Admin users only
- **Features**:
  - Create new users with names and emails
  - View all existing users
  - Auto-generate email format if needed

### 3. **Command Line User Creation**
- Easy management command for bulk user creation
- Command: `python manage.py add_user "John Doe" --email johndoe@cmr.edu.in`

### 4. **Default Password Policy**
- All new users get password: **CMRU 1**
- Users can change password after first login (through Django admin)

---

## 🚀 How to Use

### **Method 1: Web Interface**

1. Login as a staff/admin user
2. Navigate to `/admin/add-user/`
3. Fill in:
   - **Full Name**: e.g., "John Doe"
   - **Email**: e.g., "john.doe@cmr.edu.in"
4. Click "Create User"
5. Share the credentials with the user

### **Method 2: Command Line**

Run this command in your project directory:

```bash
# Basic usage (auto-generates email format)
python manage.py add_user "John Doe"

# With specific email
python manage.py add_user "John Doe" --email johndoe@cmr.edu.in

# Example output
# ✓ User created successfully!
#   Email: johndoe@cmr.edu.in
#   Password: CMRU 1
```

### **Method 3: Django Admin**

1. Go to `/admin/`
2. Click on "Users"
3. Click "Add User"
4. Fill in username as email (e.g., `john.doe@cmr.edu.in`)
5. Set password to `CMRU 1`

---

## 📋 Files Modified/Created

### New Files:
```
allocation/auth_backend.py                          # Custom authentication backend
allocation/management/commands/add_user.py          # Command-line user creation
templates/add_user.html                             # Web UI for user management
```

### Modified Files:
```
allocation/views.py                                 # Added add_user view
allocation/urls.py                                  # Added /admin/add-user/ route
classiq_project/settings.py                         # Enabled custom auth backend
templates/login.html                                # Updated with email placeholder
```

---

## 🔐 Login Flow

1. User navigates to `/login/`
2. Enters email address (e.g., `john.doe@cmr.edu.in`)
3. Enters password: `CMRU 1` (for first login)
4. System authenticates using `EmailBackend`
5. User redirected to dashboard

---

## 👤 User Management Workflow

### Creating a New User:

**Web Interface** (Recommended for admins):
- Go to `/admin/add-user/`
- Enter name and email
- System creates account with default password
- Display confirmation

**Command Line** (For system admins):
```bash
python manage.py add_user "Jane Smith" --email jane.smith@cmr.edu.in
```

**Django Admin** (For advanced management):
- Go to `/admin/auth/user/`
- Click "Add User"
- Follow on-screen prompts

---

## 🔄 User Password Changes

Users can change their password:

1. **Via Django Admin**:
   - Go to `/admin/auth/user/` (after logging in as superuser)
   - Select user
   - Click "Change password"

2. **Via Django change password view** (if implemented):
   - Add to your templates/urls.py

---

## ⚠️ Important Notes

### Email Requirements:
- Must end with `@cmr.edu.in`
- Must be unique (no duplicates)
- Recommended format: `firstname.lastname@cmr.edu.in`

### Default Password:
- Default password is: `CMRU 1`
- Users should change this after first login
- Currently no enforced password change policy (can be added)

### Staff Access:
- Only staff/superuser accounts can access `/admin/add-user/`
- To make someone staff, use Django admin interface

---

## 🐛 Troubleshooting

**Issue**: "Email must end with @cmr.edu.in"
- **Solution**: Ensure email ends with `@cmr.edu.in`

**Issue**: "User with email already exists"
- **Solution**: Each user must have unique email. Create different email or delete existing user from admin panel.

**Issue**: Login fails with correct credentials
- **Solution**: Verify email format, check if user exists in database via Django admin.

---

## 📞 Support

For issues or questions about the authentication system, check:
1. Django admin at `/admin/` for user management
2. Database via command: `python manage.py dbshell`
3. Logs for detailed error messages

---

## Summary

Your ClassIQ system now supports:
✅ Email-based login with @cmr.edu.in domain
✅ Uniform default password (CMRU 1) for new users
✅ Easy user creation via web UI or command line
✅ Full Django admin integration for user management

Enjoy your upgraded authentication system! 🎓

# Cloud Deploy (Render)
Set these environment variables in Render to auto-create a default login user on startup:
- `AUTO_CREATE_DEFAULT_USER=1`
- `DEFAULT_LOGIN_EMAIL=your.name@cmr.edu.in`
- `DEFAULT_LOGIN_PASSWORD=CMRU 1`
- `DEFAULT_LOGIN_NAME=Your Name`
Optional (for admin access):
- `DEFAULT_LOGIN_IS_STAFF=1`
- `DEFAULT_LOGIN_IS_SUPERUSER=1`

After deploy, login with the email and password above.

