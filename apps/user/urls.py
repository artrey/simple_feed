from django.urls import path, include, reverse_lazy
from django_registration.backends.one_step.views import RegistrationView

from .forms import RegistrationForm
from .views import ProfileView

app_name = 'apps.user'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegistrationView.as_view(
        form_class=RegistrationForm, success_url=reverse_lazy('accounts:profile')
    ), name='django_registration_register'),
    path('', include('django_registration.backends.one_step.urls')),
]
