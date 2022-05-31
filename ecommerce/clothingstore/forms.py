from django.forms import ModelForm 
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 

class UserForm(UserCreationForm):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"first name", "id":"firstname" ,"name":"firstname"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"last name", "id":"lastname" ,"name":"lastname"}))
    id_number =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"id number", "id":"id number" ,"name":"idnumber"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"User name", "id":"username" ,"name":"username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Email Address", "id":"email" ,"name":"email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Password", "id":"password1" ,"name":"password1"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Re-enter Password", "id":"password2" ,"name":"password2"})) 
    

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = "User name"
        self.fields['email'].label = "Email Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Re-enter Password"


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']
