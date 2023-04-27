from django.shortcuts import render, get_object_or_404
from .post import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

class post_detail(LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('post_detail')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
