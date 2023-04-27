from django.views.generic import ListView
from .models import Post

class postSearchView(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if query:
            return Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
        else:
            return Post.objects.none()
