from django.views.generic import CreateView

from apps.authentication.forms import UserCreationForm


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'authentication/registration.html'