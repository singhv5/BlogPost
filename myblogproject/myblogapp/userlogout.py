from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def userlogout(request):
    logout(request)
    return render(request, 'login.html')
