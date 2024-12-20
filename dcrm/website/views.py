from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, BookingForm, ProfileForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Custom_User, Booking
# Create your views here.

def Register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'form': form}

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
    
    context = {'login_form': form}
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
            print(valueprice)

        form = BookingForm(updated_request)

        if form.is_valid():
            obj = form.save(commit=False)
            booking_total_cost = int(obj.booking_adults) * 20 \
            + int(obj.booking_children) * 13 \
            + int(obj.booking_oap) * 17 \
            
            if valueprice == 20:
                booking_total_cost += 20
                obj.booking_path = "Short"

            elif valueprice == 45:
                booking_total_cost += 45
                obj.booking_path = "Medium"

            elif valueprice == 60:
                booking_total_cost += 60
                obj.booking_path = "Long"

            obj.booking_total_cost = booking_total_cost

            obj.save()
           
            

            return redirect('') 
        else: 
            print("wrong")

            return redirect('booking')


    context = {'Booking_form': form}

    return render(request, 'pages/booking.html', context=context, )

def index(request):
    return render(request, 'pages/index.html')

@login_required(login_url="login")
def dashboard(request):
    tablestuff = Booking.objects.filter(booking_user_id_id=request.user)
    context = {'records': tablestuff}

    return render(request, 'pages/dashboard.html', context=context)

@login_required(login_url="login")
def logout(request):
    auth.logout(request)

    return redirect('')

@login_required(login_url="login")
def profile(request):
    profilestuff = request.user

    context = {'profiledb': profilestuff}

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
    context = {'form': form}

    return render(request, 'pages/updateprofile.html', context=context)

