from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView

from apps.authentication.models import User
from apps.mine.forms import TextForm
from apps.mine.models import Text


class TextCreateView(CreateView):
    form_class = TextForm
    template_name = 'mine/text_create.html'
    success_url = reverse_lazy('initial')


# Admin views
class BaseAdminView:
    pass


class AdminRawTextListView(ListView):
    template_name = 'mine/admin/raw_texts.html'
    queryset = Text.objects.all()


class AdminRawTextCreateView(CreateView):
    form_class = TextForm
    template_name = 'mine/admin/raw_text_create.html'
    success_url = reverse_lazy('mine:admin-raw-texts')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class AdminInitialView(TemplateView):
    template_name = 'mine/admin/initial.html'


class AdminMinerListView(ListView):
    template_name = 'mine/admin/miners.html'
    queryset = User.objects.all()


class AdminModeratorListView(ListView):
    template_name = 'mine/admin/moderators.html'
    queryset = User.objects.all()