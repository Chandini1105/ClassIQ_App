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



