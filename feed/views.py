from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from . import models, forms


def signup(request):
    name = request.POST.get('name')
    if not name:
        return render(request, 'signup.html')

    request.session['name'] = name
    return redirect('feed:posts')


class CheckSignupMixin(UserPassesTestMixin):
    login_url = reverse_lazy('feed:signup')

    def handle_no_permission(self):
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

    def test_func(self):
        return bool(self.request.session.get('name'))


class Posts(CheckSignupMixin, ListView):
    template_name = 'posts.html'
    model = models.Post


class NewPost(CheckSignupMixin, FormView):
    template_name = 'new_post.html'
    form_class = forms.PostForm
    success_url = reverse_lazy('feed:posts')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.session.get('name')
        post.save()
        return super().form_valid(form)
