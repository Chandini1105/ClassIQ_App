from django.contrib import admin
from .models import Faculty, Course, Classroom, StudentLeader, Allocation


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "department")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "faculty")


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("id", "room_number", "capacity", "is_active")


@admin.register(StudentLeader)
class StudentLeaderAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Allocation)
class AllocationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "course",
        "classroom",
        "date",
        "start_time",
        "duration_minutes",
        "is_active",
    )
    