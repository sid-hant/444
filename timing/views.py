from django.shortcuts import render
from timing.models import PhilDay, ArrivalTime
from .forms import addTime
from django.contrib.auth import get_user_model
from staff.forms import schedule
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from staff.models import StaffSchedule

User = get_user_model()

# Create your views here.

def philDay(request, pk):
    phil_day = PhilDay.objects.filter(pk=pk)
    form = addTime()
    form1 = schedule()
    staff = StaffSchedule.objects.filter(day=phil_day[0]).filter(staffID=request.user)
    arrivals = ArrivalTime.objects.filter(licenseID=request.user).filter(philsDay=phil_day[0])
    confirmSchedule = False
    confirmArrival = False
    allArrivals = ArrivalTime.objects.filter(philsDay=phil_day[0])
    time = {"9 PM":0, "10 PM":0, "11 PM":0, "12 AM":0, "1 AM":0, "2 AM":0}
    for a in allArrivals:
        t = str(a.time)[0:2]
        if t == "21":
            time["9 PM"] += 1
        elif t == "22":
            time["10 PM"] += 1
        elif t == "23":
            time["11 PM"] += 1
        elif t == "00":
            time["12 AM"] += 1
        elif t == "01":
            time["1 AM"] += 1
        elif t == "02":
            time["2 AM"] += 1
    
    r = {"9 PM":0, "10 PM":0, "11 PM":0, "12 AM":0, "1 AM":0, "2 AM":0}
    for key, value in time.items():
        r[key] = (value/len(allArrivals))*100
    
    totalPeople = len(allArrivals)
    allStaff = len(StaffSchedule.objects.filter(day=phil_day[0]))
        

    
    if len(staff) == 0:
        confirmSchedule = True
    
    if len(arrivals) == 0:
        confirmArrival = True

    if request.method == "POST":
        form = addTime(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.licenseID = request.user
            f.philsDay = PhilDay.objects.get(pk=pk)
            if len(ArrivalTime.objects.filter(licenseID=request.user).filter(philsDay=phil_day[0])) != 0:
                pass
            else:
                f.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        form1 = schedule(request.POST)
        if form1.is_valid():
            f1 = form1.save(commit=False)
            f1.staffID = request.user
            f1.day = PhilDay.objects.get(pk=pk)
            if len(StaffSchedule.objects.filter(day=phil_day[0]).filter(staffID=request.user)) != 0:
                pass
            else:
                f1.save()
            return HttpResponseRedirect(reverse_lazy('home'))
    return render(request, 'day.html', {'phil_day': phil_day, 'form': form, 'form1': form1, "confirmSchedule": confirmSchedule, "confirmArrival": confirmArrival, 'staff':staff, 'arrivals':arrivals, 'time':r.items(), "totalPeople": totalPeople, 'allStaff':allStaff})