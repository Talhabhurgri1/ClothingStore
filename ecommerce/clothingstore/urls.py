from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    #django default login views 

    path('login',views.login_home,name='login'),
    path('signup',views.signup_home,name='signup'),
    path('logout',views.logout_home, name="logout"),
   
]
