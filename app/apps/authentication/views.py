from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from apps.authentication.forms import UserCreationForm


class InitialView(TemplateView):
    template_name = 'authentication/initial.html'


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'authentication/registration.html'
    success_url = reverse_lazy('initial')

    def form_valid(self, form):
        return super(RegistrationView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationView, self).form_invalid(form)


class SignInView(TemplateView):
    template_name = ''