from django.urls import path
from . import views
urlpatterns = [
    path('register', views.Register, name='register'),

    path('login', views.Login, name='login'),

    path('booking', views.Bookings, name='booking'),

    path('', views.index, name=''),

    path('dashboard', views.dashboard, name="dashboard"),

    path('logout', views.logout, name="logout"),

    path('profile', views.profile, name="profile")
]