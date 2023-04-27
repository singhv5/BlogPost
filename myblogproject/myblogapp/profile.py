from django.shortcuts import render
from .models import Profile

def profile(request):
    return render(request, 'templates/profile.html', {'user': request.user})
