from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView

from apps.authentication.models import User
from apps.mine.forms import TextForm


class TextCreateView(CreateView):
    form_class = TextForm
    template_name = 'mine/text_create.html'
    success_url = reverse_lazy('initial')


# Admin views
class BaseAdminView:
    pass


class AdminInitialView(TemplateView):
    template_name = 'mine/admin/initial.html'


class AdminMinerListView(ListView):
    template_name = 'mine/admin/miners.html'
    queryset = User.objects.all()


class AdminModeratorListView(ListView):
    template_name = 'mine/admin/moderators.html'
    queryset = User.objects.all()