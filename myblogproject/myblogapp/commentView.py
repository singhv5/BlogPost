from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .commentModel import Comment
from .forms import CommentForm

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(approved_comment=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('postcommentedListView', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'post': post, 'comments': comments, 'form': form})
