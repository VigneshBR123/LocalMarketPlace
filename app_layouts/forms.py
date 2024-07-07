from django.contrib.auth.forms import UserCreationForm
from .models import User,professionals
from django import forms
from django.forms import ModelForm

class userdetails(UserCreationForm,forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Valid Email'}))
    password1=forms.CharField(min_length=8 ,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Strong Password'}))
    password2=forms.CharField(min_length=8 ,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Your Password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class freelancer_register_page(ModelForm):
    class Meta:
        model=professionals
        fields='__all__'
