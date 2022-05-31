from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from clothingstore.decorators import unauthenticated_user
from .models import Customer
from clothingstore.models import Customer
from .forms import UserForm , CustomerForm
from django.contrib.auth import authenticate ,login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,'clothingstore/home.html')

@unauthenticated_user
def login_home(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username,password=password)
        
        if user is not None:
            print('Authenticated')
            login(request,user)
            return redirect("home")
        else:
            messages.add_message(request,messages.INFO,'Email or Password is incorrect')
            print('not authenticated')
            return redirect("login")
    return render(request,'clothingstore/login.html')

def logout_home(request):
    logout(request)
    return redirect('login')


def signup_home(request):
    
    form = UserForm()
    print('here')
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        print(f'form is{form.is_valid}')
        
        if form.is_valid:  
            user = form.save()
            Customer.objects.create(user=user,first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],id_number=form.cleaned_data['id_number'])
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.add_message(request,messages.SUCCESS, f"{form.cleaned_data['username']} has been registered")
            print('got the message')
            return redirect("login")

    context = {'form':form}
    return render(request, 'clothingstore/signup.html',context)

