from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    USER_GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices = USER_GENDER)
    city = forms.CharField()
    class meta:
        model = User
        fields = ['username','email','password1','password2','firstname' , 'lastname' , 'gender', 'city']