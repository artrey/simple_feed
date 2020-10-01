from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from . import models, forms


class Posts(LoginRequiredMixin, ListView):
    template_name = 'feed/posts.html'
    model = models.Post
    paginate_by = 10

    @property
    def current_post_id(self):
        return self.kwargs.get('post_id')

    def get_queryset(self):
        pid = self.current_post_id
        if pid:
            qs = self.model.objects.filter(parent_id=pid)
        else:
            qs = self.model.objects.root_nodes()
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        pid = self.current_post_id
        if pid:
            context.update(current_post=self.model.objects.get(id=pid))
        context.update(form=forms.PostForm())
        return context

    def post(self, request, *args, **kwargs):
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.parent_id = self.current_post_id
            post.save()
        return HttpResponseRedirect(request.path_info)
