from django import forms
from django_registration import forms as registration_forms

from . import models


class RegistrationForm(registration_forms.RegistrationForm):
    class Meta(registration_forms.RegistrationForm.Meta):
        model = models.User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = 'first_name', 'last_name', 'email',

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = True
