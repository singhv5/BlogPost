from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .post import Post 
from .rating import Rating

@login_required
def add_rating(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        value = request.POST.get('rating')
        rating, created = Rating.objects.get_or_create(post=post, user=request.user, defaults={'value': value})
        if not created:
            rating.value = value
            rating.save()
        return redirect('postRatedListView', pk=post.id)

    return render(request, 'add_rating.html', {'post': post, 'range': [1, 2, 3, 4, 5]})

@login_required
def delete_rating(request, pk):
    post = get_object_or_404(Post, pk=pk)
    rating = get_object_or_404(Rating, post=post, user=request.user)
    rating.delete()
    return redirect('postRatedListView', pk=post.pk)
