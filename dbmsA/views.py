from django.shortcuts import render, get_object_or_404
from . models import Company, BusInfo, Passenger, Seats, Rating
from . forms import SeatForm, UserForm, PassengerForm, Busform, Companyform, RatingForm
from django.contrib.auth.models import User
from json import dumps
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required                   #view required to user to logged in this decorator is used
from datetime import date, datetime
import datetime
from django.db.models import Avg
from django.contrib import messages
from django.db.models import Count


# Create your views here.

def index(request):
    if request.method == 'POST':
        s = request.POST.get('source')
        d = request.POST.get('destination')
        d1 = request.POST.get('date')
        return HttpResponseRedirect(f"searchbusesfrom{s}to{d}on{d1}")
    else:
        noofcompany = len(Company.objects.all())
        noofpassenger = len(Passenger.objects.all())
        return render(request, 'dbmsA/index.html',{"noofcompany":noofcompany, "noofpassenger":noofpassenger})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url = '/login')
def search(request, s, d, d1):
    i = BusInfo.objects.filter(source=s)
    k = i.filter(date=d1)
    j = k.filter(destination=d)
    return render(request, 'dbmsA/showavailbus.html', {'j':j, 's':s, 'd':d, 'd1':d1})

def seat(request, id):
    bus = get_object_or_404(BusInfo, id = id)
    s1 = Seats.objects.filter(busno=id)
    s = s1.filter(date = bus.date)
    a = ['S-{}'.format(x) for x in range(1,16)]
    l = ['S-{}'.format(x) for x in range(1,16)]
    a1 = a[0:5]
    a2 = a[5:10]
    a3 = a[10:]
    for i in s:
        if i.seatno in l:
            l.remove(i.seatno)
    if request.method == 'POST':
        form = SeatForm(request.POST)
        if form.is_valid():
            seat = form.save(commit=False)
            seat.busno = bus
            seat.date = bus.date
            print(bus.date)
            seat.save()
            form = SeatForm()
            return HttpResponseRedirect(f"{seat.seatno}and{id}and{seat.id}")
            #return render(request, 'dbmsA/seatbook.html', {'seat':seat,'form':form, 'id':id})
    else:
        form = SeatForm()
        c = dumps({'l':l})
        return render(request, 'dbmsA/seatbook.html',{'form':form, 'l':l,'c':c,'a':a,'a1':a1,'a2':a2,'a3':a3})

def enterdetails(request, seatno, busno, seatid):
    seat1 = get_object_or_404(Seats, id = seatid)
    bus1 = get_object_or_404(BusInfo, id=busno)
    user1 = get_object_or_404(User, username = request.user)
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        passenger = form.save(commit = False)
        passenger.seatno = seat1
        passenger.busno = bus1
        passenger.user = user1
        passenger.date = bus1.date
        passenger.save()
        return HttpResponseRedirect('/')
    
    else:
        form = PassengerForm()
        return render(request, 'dbmsA/enterdetails.html', {'form':form, 'seatid':seatid})

def updatep(request, pk):
    passenger1 = Passenger.objects.get(id=pk)
    if request.method == 'POST':
        form = PassengerForm(request.POST, instance = passenger1)
        if form.is_valid():
            passenger = form.save(commit = False)
            passenger.save()
            return HttpResponseRedirect('/books')
        
    else:
        form = PassengerForm(instance=passenger1)
        return render(request, 'dbmsA/updatep.html', {'form':form})

def books(request):   
    today = date.today()
    rate = Rating.objects.all()
    return render(request, 'dbmsA/books.html', {'today':today, "rate":rate})

def cancel(request, id):
    Seats.objects.filter(id=id).delete()
    return HttpResponseRedirect('/')

def cancelbooks(request, id):
    Seats.objects.filter(id=id).delete()
    return HttpResponseRedirect('/books')


def deletecompany(request, id):
    Company.objects.filter(id=id).delete()
    return HttpResponseRedirect('/viewbooks')

def deletebus(request, id):
    BusInfo.objects.filter(id=id).delete()
    return HttpResponseRedirect('/viewbooks')

def deletepassenger(request, id):
    passenger = get_object_or_404(Passenger, id=id)
    seatno = passenger.seatno
    seat = get_object_or_404(Seats, seatno = seatno)
    Seats.objects.filter(id=seat.id).delete()
    return HttpResponseRedirect('/viewbooks')

def addcompany(request):
    i = date.today()
    form = Companyform()
    if request.method == "POST":
        form1 = Companyform(request.POST)
        name = request.POST.get("name")
        if Company.objects.filter(name = name).exists():
            messages.info(request, "Company name already exists")
            return render(request, 'dbmsA/addcompany.html', {'form':form})
        else:
            if form1.is_valid():
                form = form1.save(commit=False)
                form.registereddate = i
                form.save()
                form = Companyform()
                return render(request, 'dbmsA/addcompany.html', {'form':form})

    else:
        form = Companyform()
        return render(request, 'dbmsA/addcompany.html', {'form':form})

def addbus(request):
    if request.method == "POST":
        form = Busform(request.POST)
        busno = request.POST.get("busno")
        date = request.POST.get("date")
        b = BusInfo.objects.filter(date = date)

        if b.filter(busno = busno).exists():
            form = Busform()
            messages.info(request, f"Bus with Number {busno} already registered on{date}")
            return render(request, 'dbmsA/addbus.html', {'form':form})

        else:
            if form.is_valid():
                form.save()
                form = Busform()
                return render(request, 'dbmsA/addbus.html', {'form':form})

    else:
        form = Busform()
        return render(request, 'dbmsA/addbus.html', {'form':form})

def viewbooks(request):
        company = Company.objects.all()
        bus = BusInfo.objects.all()
        passenger = Passenger.objects.all()
        return render(request, 'dbmsA/viewbooks.html', {'company':company,'bus':bus,'passenger':passenger,'viewbooks':viewbooks})

def register(request):
    form = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        username = request.POST.get("username")
        email = request.POST.get("email")

        if User.objects.filter(username = username).exists() and User.objects.filter(email = email):
            messages.info(request, "Username and Email already exists")
            return render(request, 'dbmsA/register.html', {'form':form})

        elif User.objects.filter(username = username).exists():
            messages.info(request, "Username already exists")
            return render(request, 'dbmsA/register.html', {'form':form})

        elif User.objects.filter(email = email).exists():
            messages.info(request, "Email already exists")
            return render(request, 'dbmsA/register.html', {'form':form})

        else:
            if userform.is_valid():
                user = userform.save()
                user.set_password(user.password)
                user.save()
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
        return render(request, 'dbmsA/register.html', {'form':form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                if 'next' in request.POST:
                    return HttpResponseRedirect(request.POST.get('next'))
                else:
                    return HttpResponseRedirect('/')
            
            else:
                return HttpResponse('User not active')

        else:
            messages.info(request, "Invalid credentials")
            return render(request, 'dbmsA/login.html')

    else:
        return render(request, 'dbmsA/login.html')

def orderby(request, s, d, d1, orderby):
    i = BusInfo.objects.filter(source=s)
    k = i.filter(date=d1)
    #j = k.filter(destination=d).order_by("price").reverse()

    if orderby == "rating":
        j = k.filter(destination=d).order_by("rate").reverse()
    if orderby == "cheap":
        j = k.filter(destination=d).order_by("price")
    if orderby == "expensive":
        j = k.filter(destination=d).order_by("price").reverse()
    if orderby == "ac":
        j1 = k.filter(destination=d)
        j = j1.filter(bustype = "AC")
    if orderby == "nonac":
        j1 = k.filter(destination=d)
        j = j1.filter(bustype = "NON AC")

    return render(request, 'dbmsA/showavailbus.html', {'j':j, 's':s, 'd':d, 'd1':d1})

def rating(request, passid, busid):
    passenger1 = get_object_or_404(Passenger, id = passid)
    bus1 = get_object_or_404(BusInfo, id = busid)
    busno = bus1.busno
    avgrate = Rating.objects.filter(bus=busid).aggregate(Avg('rate'))
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit = False)
            rate.passenger = passenger1
            rate.bus = bus1
            rate.save()
            avgrate = Rating.objects.filter(bus=busid).aggregate(Avg('rate'))

            BusInfo.objects.filter(busno = busno).update(rate = avgrate["rate__avg"])
            return HttpResponseRedirect("/books")

    else:
        form = RatingForm()
        rate = Rating.objects.filter(passenger = passenger1).exists()
        return render(request, 'dbmsA/rating.html', {"form":form, "avgrate":avgrate, "rate":rate, "passenger1":passenger1, "bus1":bus1})



    




# n = request.POST.get('name')
# g = request.POST.get('gender')
# a = request.POST.get('age')
# e = request.POST.get('emailid')
# p = request.POST.get('phoneno')
# t = Passenger(name=n, gender=g, age=a, emailid=e, phoneno=p, seatno=seat1, busno=bus1)
# t.save()
# request.user.passenger.add(t)

#changed index, seat, rating
#changed index.html, seatbook.html, showavailbus.htm
#changed model rating and businfo str

