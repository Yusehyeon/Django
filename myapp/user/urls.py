from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    #user
    path('register/', views.Registration.as_view(), name='register'),
    #Login
    path('login/', views.Login.as_view(), name='login'),
    #Logout
    path('logout/', views.Logout.as_view(), name='logout'),

]