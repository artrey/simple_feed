from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from . import models, forms


class Posts(LoginRequiredMixin, ListView):
    template_name = 'feed/posts.html'
    model = models.Post
    paginate_by = 5

    @property
    def parent_id(self):
        return self.kwargs.get('parent')

    def get_queryset(self):
        pid = self.parent_id
        if pid:
            qs = self.model.objects.filter(parent_id=pid)
        else:
            qs = self.model.objects.root_nodes()
        return qs

    def post(self, request, *args, **kwargs):
        self.model.objects.create(body=request.POST.get('body'),
                                  author=request.user, parent_id=self.parent_id)
        return HttpResponseRedirect(request.path_info)


class NewPost(LoginRequiredMixin, FormView):
    template_name = 'feed/new_post.html'
    form_class = forms.PostForm
    success_url = reverse_lazy('feed:posts')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.session.get('name')
        post.save()
        return super().form_valid(form)
