from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .post import Post
from django.urls import reverse_lazy

class postCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('postListView')
