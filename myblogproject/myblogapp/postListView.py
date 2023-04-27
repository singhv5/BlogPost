from django.views.generic import ListView
from .post import Post
from .rating import Rating
from .commentModel import Comment

class postListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rating'] = Rating.objects.all()
        context['comment'] = Comment.objects.all()
        return context
