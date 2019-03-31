from django import forms
from staff.models import StaffSchedule 


class schedule(forms.ModelForm):
    class Meta():
        model = StaffSchedule
        fields = ()
        labels = {}
        widgets = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

