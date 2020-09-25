from django.urls import reverse_lazy
from django.views.generic import FormView
from . import forms


class ProfileView(FormView):
    form_class = forms.ProfileForm
    template_name = 'user/profile.html'
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self) -> dict:
        kwargs = super().get_form_kwargs()
        kwargs.update(instance=self.request.user)
        return kwargs
