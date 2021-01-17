from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Event

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['profile']