from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from . import models, forms


class Posts(LoginRequiredMixin, ListView):
    template_name = 'feed/posts.html'
    model = models.Post


class NewPost(LoginRequiredMixin, FormView):
    template_name = 'feed/new_post.html'
    form_class = forms.PostForm
    success_url = reverse_lazy('feed:posts')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.session.get('name')
        post.save()
        return super().form_valid(form)
