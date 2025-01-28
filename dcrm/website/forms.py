from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Custom_User, Booking, Payment

from django import forms
from django.forms.widgets import PasswordInput, TextInput

class RegisterForm(UserCreationForm):
    class Meta:
        model = Custom_User
        fields = ['username','first_name','last_name','email', 'phonenum', 'password1', 'password2']

        labels = {
            'phonenum' : 'Phone Number', }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = ['booking_user_id','booking_date', 'booking_adults','booking_children','booking_oap','booking_total_cost']

        widgets = {'booking_date': forms.DateInput(attrs={'type': 'date'}),
                   'booking_total_cost' : forms.HiddenInput(),
                   'booking_user_id': forms.HiddenInput(),}
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Custom_User

        fields = ['username','first_name','last_name','email', 'phonenum']

        
        