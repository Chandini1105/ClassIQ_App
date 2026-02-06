from django.db import models
from datetime import datetime, timedelta, time
from django.utils import timezone

# Time Slot Configuration
SCHOOL_START_TIME = time(8, 30)      # 8:30 AM
SCHOOL_END_TIME = time(16, 30)       # 4:30 PM

class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=20, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("name", "faculty")

    def __str__(self):
        return f"{self.name}"

class Classroom(models.Model):
    room_number = models.CharField(max_length=20, unique=True)
    capacity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number
    
    def get_available_status(self, date_obj=None, time_obj=None):
        """Check if classroom is available at given time"""
        if date_obj is None:
            date_obj = timezone.now().date()
        if time_obj is None:
            time_obj = timezone.now().time()
        
        # Check if time is within college hours (8:30 AM - 4:30 PM)
        if not (SCHOOL_START_TIME <= time_obj < SCHOOL_END_TIME):
            return False  # Outside college hours
        
        # Check if there's any conflicting allocation
        conflicting = Allocation.objects.filter(
            classroom=self,
            date=date_obj
        ).exists()
        
        if not conflicting:
            return True
        
        # Check for specific time conflict
        for allocation in Allocation.objects.filter(classroom=self, date=date_obj):
            alloc_start = allocation.start_time
            alloc_end_dt = datetime.combine(date_obj, allocation.start_time) + timedelta(minutes=allocation.duration_minutes)
            alloc_end = alloc_end_dt.time()
            
            if alloc_start <= time_obj < alloc_end:
                return False
        
        return True

class StudentLeader(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Allocation(models.Model):
    student_leader = models.ForeignKey(
        StudentLeader, on_delete=models.SET_NULL, null=True
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    date = models.DateField()
    start_time = models.TimeField()
    duration_minutes = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def end_time(self):
        start = datetime.combine(self.date, self.start_time)
        return start + timedelta(minutes=self.duration_minutes)

    def is_active(self):
        now = timezone.now()
        tz = timezone.get_current_timezone()
        start_naive = datetime.combine(self.date, self.start_time)
        end_naive = self.end_time()
        
        start = timezone.make_aware(start_naive, timezone=tz)
        end = timezone.make_aware(end_naive, timezone=tz)
        return start <= now <= end

    is_active.boolean = True

    def __str__(self):
        return f"{self.classroom} | {self.course} | {self.date}"

