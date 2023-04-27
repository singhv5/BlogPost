from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def user_logout(request):
    logout(request)
    return redirect('home')
