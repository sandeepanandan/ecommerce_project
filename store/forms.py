from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms




class UserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':"text",'id':"form3Example1c" ,'placeholder':'Your Name'}))
    email    = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','type':"email",'id':"form3Example1c" ,'placeholder':'Your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':"password",'id':"form3Example1c" ,'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':"password",'id':"form3Example1c" ,'placeholder':'Reapet Your Password'}))
    
    class meta:
        model = User
        fields = [
            'first_name',
            'email',
            'password1',
            'password2',
        ]


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':"text",'id':"form3Example1c" ,'placeholder':'UserName'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':"password",'id':"form3Example1c" ,'placeholder':'Password'}))




