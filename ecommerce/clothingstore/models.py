from msvcrt import open_osfhandle
from django.db import models
import datetime
from django.forms import DateField
from django.contrib.auth.models import User, AbstractBaseUser,PermissionsMixin , BaseUserManager


# Create your models here.
#models are customer/product/order

class Customer(models.Model):

    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,null=False, blank=False)
    last_name = models.CharField(max_length=30,null=False, blank=False)
    
    date_created = models.DateTimeField(auto_now_add=True)
    profilepic =models.ImageField(null=True,blank=True)
    id_number = models.CharField(max_length=20,blank=False,null=False)



    def __str__(self):
        return f"{self.first_name +' ' + self.last_name}"
        
'''
class CustomAccountManager(BaseUserManager):
    def create_user(self,email,user_name,first_name,last_name,password , **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email,user_name=user_name,first_name = first_name , last_name = last_name,password=password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,user_name,first_name,last_name,password , **other_fields):
        
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)

        if other_fields.setdefault('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.setdefault('is_active') is not True:
            raise ValueError('Superuser must be assigned to is_active=True') 
        if other_fields.setdefault('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')


class CustomUser(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(('email address'),unique=True)
    user_name = models.CharField(max_length=30,unique=True)
    first_name = models.CharField(max_length=30,null=False, blank=False)
    last_name = models.CharField(max_length=30,null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    profilepic =models.ImageField(null=True,blank=True)
    id_number = models.CharField(max_length=30,blank=False,null=False,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','user_name']
    def __str__(self):
        return f'User {self.username}'


'''