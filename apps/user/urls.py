from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView

from .forms import RegistrationForm
from .views import ProfileView

app_name = 'apps.user'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegistrationView.as_view(
        form_class=RegistrationForm,
    ), name="django_registration_register"),
]
