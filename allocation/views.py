from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, get_user_model
from django.utils import timezone
from django.contrib import messages
from django.db.models import Value
from django.db.models.functions import Replace, Upper
from datetime import datetime, date, time, timedelta
import os

from .models import (
    Faculty,
    Course,
    Classroom,
    StudentLeader,
    Allocation,
    SCHOOL_START_TIME,
    SCHOOL_END_TIME,
)
from .forms import AllocationForm

User = get_user_model()
DEFAULT_PASSWORD = "CMRU 1"

def get_available_classrooms(date_obj=None, exclude_time_ranges=None):
    """
    Get classrooms currently available.
    If date_obj is provided, filters for that date.
    exclude_time_ranges: list of (start_time, end_time) tuples to exclude
    """
    local_now = timezone.localtime()
    if date_obj is None:
        date_obj = local_now.date()

    current_time = local_now.time()
    
    # Get all active classrooms
    all_rooms = Classroom.objects.filter(is_active=True)
    available = []
    
    for room in all_rooms:
        # Check if there are any conflicting allocations
        allocations = Allocation.objects.filter(
            classroom=room,
            date=date_obj
        )
        
        is_available = True
        for alloc in allocations:
            alloc_start = alloc.start_time
            alloc_end_dt = datetime.combine(date_obj, alloc.start_time) + timedelta(minutes=alloc.duration_minutes)
            alloc_end = alloc_end_dt.time()
            
            # Check if current time falls within any booking
            if alloc_start <= current_time < alloc_end:
                is_available = False
                break
        
        if is_available:
            available.append(room)
    
    return available

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def dashboard(request):
    now = timezone.localtime()
    today = now.date()

    # Get all allocations for today
    all_allocations = Allocation.objects.filter(date=today)

    ongoing = []
    upcoming = []
    busy_rooms = []

    tz = timezone.get_current_timezone()
    for a in all_allocations:
        start_naive = datetime.combine(a.date, a.start_time)
        end_naive = a.end_time()
        
        start = timezone.make_aware(start_naive, timezone=tz)
        end = timezone.make_aware(end_naive, timezone=tz)

        if start <= now < end:
            ongoing.append(a)
            busy_rooms.append(a.classroom_id)
        elif start > now:
            upcoming.append(a)

    # Get available rooms based on current time
    available_rooms = get_available_classrooms(today)

    # Get all classrooms with availability status
    # A classroom is unavailable only when there is an active booking right now.
    all_classrooms = Classroom.objects.filter(is_active=True).order_by('room_number')
    classroom_status = []
    
    for room in all_classrooms:
        # Check if classroom has any active or upcoming booking
        is_available = True
        room_allocations = Allocation.objects.filter(classroom=room, date=today)
        
        for alloc in room_allocations:
            alloc_start = alloc.start_time
            alloc_end_dt = datetime.combine(today, alloc.start_time) + timedelta(minutes=alloc.duration_minutes)
            alloc_end = alloc_end_dt.time()

            # Unavailable only during the booking window.
            if alloc_start <= now.time() < alloc_end:
                is_available = False
                break
        
        classroom_status.append({
            'room': room,
            'is_available': is_available
        })
    
    # Count currently available classrooms.
    available_count = sum(1 for item in classroom_status if item['is_available'])

    return render(request, "dashboard.html", {
        "ongoing_classes": ongoing,
        "upcoming_classes": upcoming,
        "available_rooms": available_rooms,
        "all_allocations": all_allocations,
        "active_count": len(ongoing),
        "available_count": available_count,
        "classroom_status": classroom_status,
        "current_time": now,
        "school_start": SCHOOL_START_TIME,
        "school_end": SCHOOL_END_TIME,
    })

@login_required
def help(request):
    """Display help and support page"""
    return render(request, "help.html")

@login_required
def book_classroom(request):
    form = AllocationForm(request.POST or None)

    if form.is_valid():
        data = form.cleaned_data

        # Validate time is within college hours (8:30 AM - 4:30 PM)
        booking_date = data["date"]
        start_time = data["start_time"]
        duration = data["duration_minutes"]
        
        # Calculate end time
        end_dt = datetime.combine(booking_date, start_time) + timedelta(minutes=duration)
        end_time = end_dt.time()
        
        # Check if start time is within college hours
        if not (SCHOOL_START_TIME <= start_time < SCHOOL_END_TIME):
            form.add_error("start_time", f"Classes must start between {SCHOOL_START_TIME.strftime('%H:%M')} and {SCHOOL_END_TIME.strftime('%H:%M')}")
            return render(request, "book_classroom.html", {"form": form})
        
        # Check if end time exceeds college hours
        if end_time > SCHOOL_END_TIME:
            form.add_error("duration_minutes", f"Classes must end by {SCHOOL_END_TIME.strftime('%H:%M')}. Reduce duration.")
            return render(request, "book_classroom.html", {"form": form})

        # Student (free text)
        student_leader = None
        if data["student_leader"]:
            student_leader, _ = StudentLeader.objects.get_or_create(
                name=data["student_leader"].strip()
            )
        # Faculty (free text)
        faculty, _ = Faculty.objects.get_or_create(
            name=data["faculty"].strip()
        )
        # Course (free text) - handle multiple existing courses
        course_name = data["course"].strip()
        course = Course.objects.filter(
            name=course_name,
            faculty=faculty
        ).first()
        if not course:
            course = Course.objects.create(
                name=course_name,
                faculty=faculty
            )
        # Classroom MUST exist. Match case-insensitively and ignore spaces.
        entered_classroom = data["classroom"].strip()
        normalized_entered = "".join(entered_classroom.split()).upper()

        classroom = Classroom.objects.filter(
            room_number__iexact=entered_classroom
        ).first()

        if not classroom:
            classroom = (
                Classroom.objects.annotate(
                    normalized_room_number=Upper(
                        Replace("room_number", Value(" "), Value(""))
                    )
                )
                .filter(normalized_room_number=normalized_entered)
                .first()
            )

        if not classroom:
            # Bootstrap fallback for fresh deployments without classroom seed data.
            if not Classroom.objects.exists() and entered_classroom:
                default_capacity = int(os.environ.get("DEFAULT_CLASSROOM_CAPACITY", "60"))
                classroom = Classroom.objects.create(
                    room_number=entered_classroom,
                    capacity=default_capacity,
                    is_active=True,
                )
                messages.info(
                    request,
                    f"Created first classroom '{classroom.room_number}' with capacity {classroom.capacity}.",
                )

        if not classroom:
            available_rooms = list(
                Classroom.objects.filter(is_active=True)
                .order_by("room_number")
                .values_list("room_number", flat=True)[:10]
            )
            if available_rooms:
                form.add_error(
                    "classroom",
                    f"Classroom does not exist. Try one of: {', '.join(available_rooms)}",
                )
            else:
                form.add_error("classroom", "No active classrooms found. Please contact admin.")
            return render(request, "book_classroom.html", {"form": form})
        
        allocation = Allocation(
            student_leader=student_leader,
            course=course,
            classroom=classroom,
            date=booking_date,
            start_time=start_time,
            duration_minutes=duration,
        )
        
        # Check for conflicting bookings
        
        # Check for conflicting allocations
        conflicting_allocations = Allocation.objects.filter(
            classroom=classroom,
            date=booking_date,
        )
        
        conflict = False
        for existing in conflicting_allocations:
            existing_end = datetime.combine(existing.date, existing.start_time) + timedelta(minutes=existing.duration_minutes)
            existing_end_time = existing_end.time()
            
            # Check if time slots overlap
            if (start_time < existing_end_time and end_time > existing.start_time):
                conflict = True
                break

        if conflict:
            form.add_error(None, "This classroom is already booked for this time slot.")
        else:
            allocation.save()
            messages.success(request, f"✓ Classroom {classroom.room_number} booked successfully!")
            return redirect("dashboard")

    return render(request, "book_classroom.html", {"form": form, "school_start": SCHOOL_START_TIME, "school_end": SCHOOL_END_TIME})

@login_required
@login_required
def active_classes(request):
    now = timezone.localtime()
    today = now.date()

    # Get all allocations for today (booked classes)
    allocations = Allocation.objects.filter(date=today).order_by('start_time')
    
    # Add status to each allocation
    tz = timezone.get_current_timezone()
    allocations_with_status = []
    
    for alloc in allocations:
        start_naive = datetime.combine(alloc.date, alloc.start_time)
        end_naive = alloc.end_time()
        
        start = timezone.make_aware(start_naive, timezone=tz)
        end = timezone.make_aware(end_naive, timezone=tz)
        
        if start <= now < end:
            status = "Active"
        elif end < now:
            status = "Completed"
        else:
            status = "Upcoming"
        
        allocations_with_status.append({
            'allocation': alloc,
            'status': status,
            'start': start,
            'end': end
        })

    return render(request, "active_classes.html", {"allocations": allocations_with_status})


@login_required
def add_user(request):
    """Admin view to create new users with default password"""
    # Check if user is superuser/staff
    if not request.user.is_staff:
        return redirect('dashboard')    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        
        if not name or not email:
            messages.error(request, 'Name and email are required.')
            return render(request, 'add_user.html')
        
        if not email.endswith('@cmr.edu.in'):
            messages.error(request, 'Email must end with @cmr.edu.in')
            return render(request, 'add_user.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, f'User with email {email} already exists!')
            return render(request, 'add_user.html')
        
        try:
            name_parts = name.split()
            first_name = name_parts[0] if len(name_parts) > 0 else name
            last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''
            
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=DEFAULT_PASSWORD
            )
            messages.success(
                request, 
                f'✓ User created! Email: {email} | Password: {DEFAULT_PASSWORD}'
            )
            return redirect('add_user')
        except Exception as e:
            messages.error(request, f'Error creating user: {str(e)}')
            return render(request, 'add_user.html')
    
    # Show existing users
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'add_user.html', {'users': users})


