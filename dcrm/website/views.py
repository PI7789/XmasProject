from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, BookingForm, ProfileForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Custom_User, Booking
import requests
from datetime import datetime,timedelta
# Create your views here.

def Register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    forecast,daystime = api()
    context = {'form': form,
               'forecast': forecast,
               'day': daystime}

    return render(request,'pages/Register.html', context=context)
    

def Login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('')
    forecast,daystime = api()
    context = {'forecast': forecast,
               'day': daystime,
               'login_form': form}
    
    return render(request,'pages/login.html', context=context)

@login_required(login_url = "login")
def Bookings(request):
    form = BookingForm()
    
    
    if request.method == "POST":
        print("on booking")
        updated_request = request.POST.copy()
        updated_request.update({'booking_user_id': request.user})
        if "short_path" in request.POST:
            
            valueprice = request.POST['short_path']
        elif "medium_path" in request.POST:

            valueprice = request.POST['medium_path']

        elif "long_path" in request.POST:

            valueprice = request.POST['long_path']
        form = BookingForm(updated_request)

        if form.is_valid():
            obj = form.save(commit=False)
            booking_total_cost = int(obj.booking_adults) * 20 \
            + int(obj.booking_children) * 13 \
            + int(obj.booking_oap) * 17 \
            
            if valueprice == "short_path":
                booking_total_cost += 20
                booking_path = "Short"

            elif valueprice == "medium_path":
                booking_total_cost += 35
                booking_path = "Medium"

            elif valueprice == "long_path":
                booking_total_cost += 50
                booking_path = "Long"

            

            obj.booking_total_cost = booking_total_cost
            obj.booking_path = booking_path

            obj.save()
        
            

            return redirect('') 
        else: 
            print("wrong")

            return redirect('booking')
    forecast,daystime = api()
    context = {'forecast': forecast,
               'day': daystime,
               'Booking_form': form}

    return render(request, 'pages/booking.html', context=context, )

def index(request):
    forecast, daystime = api()
    context = {'forecast': forecast,
               'day': daystime}
    return render(request, 'pages/index.html', context=context)

@login_required(login_url="login")
def dashboard(request):
    tablestuff = Booking.objects.filter(booking_user_id_id=request.user)
    forecast, daystime = api()
    context = {'forecast': forecast,
               'day': daystime,
               'records': tablestuff}

    return render(request, 'pages/dashboard.html', context=context)

@login_required(login_url="login")
def logout(request):
    auth.logout(request)

    return redirect('')

@login_required(login_url="login")
def profile(request):
    profilestuff = request.user
    forecast, daystime = api()
    context = {'forecast': forecast,
               'day': daystime,
               'profiledb': profilestuff}

    return render(request, 'pages/profile.html', context=context)
    
@login_required(login_url="login")
def updateprofile(request):
    form = ProfileForm(instance=request.user)

    if request.method=="POST":

        form = ProfileForm(request.POST, instance=request.user)

        print(form.errors)
        if form.is_valid():
            print("UPDATE PROFILE: Form is valid")
            print(request.POST)
            
            form.save()
            print(form.errors)
        else:
            print("UPDATE PROFILE: Form is NOT valid")
            



        return redirect('profile')
    forecast, daystime = api()
    context = {'forecast': forecast,
               'day': daystime,
               'form': form}

    return render(request, 'pages/updateprofile.html', context=context)

def api():
    api_key = 'XJ5M8W629NUZWX4UFYWER9SKS'
    city = "Rovaniemi"

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/?key={api_key}"
    response = requests.get(url)
    data = response.json()

    todayunformatted = datetime.now()
    
    

    daystime = []

    for y in range(0,7):
        day = todayunformatted + timedelta(days=y)
        today = day.strftime("%b %d")
        daystime.append(today)


    forecast = []

    for x in range(0,7):
        celcius = (data['days'][x]['temp'] - 32) * 5 / 9
        Weather_Data = {
        'temp' : round(celcius, 1),
        'icon_code' : data['days'][x]['icon'],
        'desc' : data['days'][x]['conditions'],
        }
        forecast.append(Weather_Data)

    
       
    return forecast, daystime