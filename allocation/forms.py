from django import forms
from .models import Classroom

class AllocationForm(forms.Form):
    student_leader = forms.CharField(required=False)
    faculty = forms.CharField(required=True)
    course = forms.CharField(required=True)
    classroom = forms.ModelChoiceField(
        queryset=Classroom.objects.none(),
        empty_label="Select a classroom",
        required=True,
    )

    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    duration_minutes = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["classroom"].queryset = Classroom.objects.filter(
            is_active=True
        ).order_by("room_number")


class CancelBookingForm(forms.Form):
    student_name = forms.CharField(required=True, max_length=100)
    faculty_name = forms.CharField(required=True, max_length=100)
    reason = forms.CharField(required=True, widget=forms.Textarea(attrs={"rows": 3}))

    def __init__(self, *args, **kwargs):
        self.expected_faculty = (kwargs.pop("expected_faculty", None) or "").strip()
        self.expected_student = (kwargs.pop("expected_student", None) or "").strip()
        super().__init__(*args, **kwargs)

        self.fields["student_name"].widget.attrs.update({"placeholder": "Enter student leader name"})
        self.fields["faculty_name"].widget.attrs.update({"placeholder": "Enter faculty name"})
        self.fields["reason"].widget.attrs.update({"placeholder": "Reason for cancellation"})

    def clean_faculty_name(self):
        faculty_name = (self.cleaned_data.get("faculty_name") or "").strip()
        if self.expected_faculty and faculty_name.lower() != self.expected_faculty.lower():
            raise forms.ValidationError("Faculty name does not match this booking.")
        return faculty_name

    def clean_student_name(self):
        student_name = (self.cleaned_data.get("student_name") or "").strip()
        if self.expected_student and student_name.lower() != self.expected_student.lower():
            raise forms.ValidationError("Student name does not match this booking.")
        return student_name



