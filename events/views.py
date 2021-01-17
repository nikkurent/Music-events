from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm, CreateEventForm

# Create your views here.
def home_view(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'home.html', context)


def register_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            Profile.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Or password is incorect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def create_event_view(request):
    user = request.user
    form = CreateEventForm()
    if request.method == 'POST':
        form = CreateEventForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit = False)
            form.profile = user.profile
            form.save()
            return redirect('home')
            
    context = {
        'form': form
    }
    return render(request, 'create_event.html', context)

def event_view(request, name):
    event = Event.objects.get(name = name)
    context = {
        'event': event
    }
    return render(request, 'event.html', context )