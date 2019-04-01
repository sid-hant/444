from django.shortcuts import render
from timing.models import PhilDay, ArrivalTime
from staff.models import StaffSchedule
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import datetime
from user.models import Ban

# Create your views here.
def dashboard(request):
    ban = Ban.objects.filter(licenseID=request.user)
    flag = True
    if len(ban)==0:
        flag=False
    day = PhilDay.objects.filter(startDay__gte=datetime.today())
    signedUp = ArrivalTime.objects.filter(licenseID = request.user).filter(philsDay__startDay__gte=datetime.today())
    staffSchedule = StaffSchedule.objects.filter(staffID = request.user).filter(day__startDay__gte=datetime.today())
    return render(request, 'dashboard.html', {'flag':flag,'phil_days': day, 'signedUp': signedUp, 'staffSchedule': staffSchedule})

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
                alert = " ERROR INFO WAS NOT VALID"
                return render(request, 'user-signup.html',{'form': form,'alert': alert})
        else:
            form = SignUpForm()
            alert = " ERROR INFO WAS NOT VALID"
            print(alert)
            return render(request, 'user-signup.html',{'form': form,'alert': alert})
        return render(request, 'user-signup.html',{'form': form})