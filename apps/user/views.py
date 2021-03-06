import typing
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from . import forms


class ProfileView(LoginRequiredMixin, FormView):
    form_class = forms.ProfileForm
    template_name = 'user/profile.html'

    def form_valid(self, form):
        form.save()
        return self.render_to_response(self.get_context_data(success=True))

    def get_form_kwargs(self) -> typing.Dict[str, typing.Any]:
        kwargs = super().get_form_kwargs()
        kwargs.update(instance=self.request.user)
        return kwargs
