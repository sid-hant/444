from django import forms
from timing.models import ArrivalTime 


class addTime(forms.ModelForm):
    class Meta():
        model = ArrivalTime
        fields = ('time',)
        labels = {
            'time': 'Approx. Arrival Time',
        }
        widgets = {
            'time': forms.DateInput(attrs={'type': 'time'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


