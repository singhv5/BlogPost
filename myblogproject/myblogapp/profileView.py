from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from .post import Post
from django.views.generic import ListView
from django.contrib.auth.models import User

def profile_view(request, username):
    # get the user object for the requested user
    user = User.objects.get(username=username)

    # get the posts authored by the requested user
    posts = Post.objects.filter(author=user)

    context = {
        'user': user,
        'posts': posts,
    }

    return render(request, 'profile.html', context)

class profileListView(ListView):
    model = Post
    template_name = 'profile.html'
    context_object_name = 'posts'
    ordering = ['-created_date']