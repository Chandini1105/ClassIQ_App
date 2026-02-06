from django import forms

class AllocationForm(forms.Form):
    student_leader = forms.CharField(required=False)
    faculty = forms.CharField(required=True)
    course = forms.CharField(required=True)
    classroom = forms.CharField(required=True)

    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))
    duration_minutes = forms.IntegerField(min_value=1)



