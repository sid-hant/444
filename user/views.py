from django.shortcuts import render
from timing.models import PhilDay, ArrivalTime
from staff.models import StaffSchedule
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
def dashboard(request):
    day = PhilDay.objects.filter()
    signedUp = ArrivalTime.objects.filter(licenseID = request.user)
    staffSchedule = StaffSchedule.objects.filter(staffID = request.user)
    return render(request, 'dashboard.html', {'phil_days': day, 'signedUp': signedUp, 'staffSchedule': staffSchedule})

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('home'))
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                return HttpResponseRedirect(reverse_lazy('home'))
        else:
            form = SignUpForm()
        return render(request, 'user-signup.html',{'form': form})