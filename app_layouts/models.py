from django.db import models
from django.contrib.auth.models import User
import datetime
import os
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "br20022006@gmail.com", "vicky@123")


def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Profession(models.Model):
    Profession_category=models.CharField(max_length=150,null=False,blank=False)
    Image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    Description=models.TextField(max_length=750,null=True,blank=True)
    Status=models.BooleanField(default=False,help_text="0-show status || 1- hidden")
    Emergant_freelancer=models.BooleanField(default=True,help_text="0-show status || 1- hidden")
    Created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Profession_category

class professionals(models.Model):
    Profession=models.ForeignKey(Profession,on_delete=models.CASCADE)
    Name=models.CharField(max_length=150,null=False,blank=False)
    Image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    My_Profession=models.CharField(max_length=150,null=False,blank=False)
    About_me=models.TextField(max_length=1000,null=False,blank=False)
    Qualification=models.CharField(max_length=1000,null=False,blank=False)
    Skills=models.CharField(max_length=1000,null=False,blank=False)
    Experiance=models.TextField(max_length=750,null=True,blank=True)
    Address_1=models.CharField(max_length=150,null=False,blank=False)
    Address_2=models.CharField(max_length=150,null=False,blank=False)
    District=models.CharField(max_length=150,null=False,blank=False)
    State=models.CharField(max_length=150,null=False,blank=False)
    Country=models.CharField(max_length=150,null=False,blank=False)
    GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('O', 'Other')
    )
    Gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    Age=models.PositiveIntegerField(max_length=2,null=False,blank=False)
    Payment=models.PositiveIntegerField(max_length=5,null=False,blank=False)
    Adhar_number=models.CharField(max_length=12,null=False,blank=False)
    Adhar_image=models.ImageField(upload_to=getFileName,null=False,blank=False)
    Phone_number=models.CharField(max_length=10,null=False,blank=False)
    WhatsApp_number=models.CharField(max_length=10,null=False,blank=False)
    Email=models.EmailField(null=False,blank=False)
    Linkedin=models.URLField(max_length=150,null=True,blank=True)
    Status=models.BooleanField(default=False,help_text="0-show status || 1- hidden")
    Availabe_any_time=models.BooleanField(default=True,help_text="If Available Click Checkbox")
    Emergant_freelancer=models.BooleanField(default=True,help_text="If You Are A Emergent Worker Click Checkbox")
    Created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Name

class specialist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profession=models.ForeignKey(professionals,on_delete=models.CASCADE)
    Created_at=models.DateTimeField(auto_now_add=True)
