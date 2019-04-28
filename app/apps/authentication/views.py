from django.contrib import messages
from django.views.generic import CreateView, TemplateView

from apps.authentication.forms import UserCreationForm


class InitialView(TemplateView):
    template_name = 'authentication/initial.html'


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'authentication/registration.html'

    def form_valid(self, form):
        messages.success(self.request, 'success')
        return super(RegistrationView, self).form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'failure')
        return super(RegistrationView, self).form_invalid(form)