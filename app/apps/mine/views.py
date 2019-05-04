from braces.views import GroupRequiredMixin as BaseGroupRequiredMixin, SuperuserRequiredMixin
from django.db.models import Q

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
class BaseAdminView(SuperuserRequiredMixin):
    pass


class AdminRawTextListView(BaseAdminView, ListView):
    template_name = 'mine/admin/raw_texts.html'
    queryset = Text.objects.all()


class AdminRawTextCreateView(BaseAdminView, CreateView):
    form_class = TextForm
    template_name = 'mine/admin/raw_text_create.html'
    success_url = reverse_lazy('mine:admin-raw-texts')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class AdminInitialView(BaseAdminView, TemplateView):
    template_name = 'mine/admin/initial.html'


class AdminMinerListView(BaseAdminView, ListView):
    template_name = 'mine/admin/miners.html'
    queryset = User.objects.filter(Q(is_superuser=True) | Q(groups__name='miner')).order_by('id')


class AdminModeratorListView(BaseAdminView, ListView):
    template_name = 'mine/admin/moderators.html'
    queryset = User.objects.filter(Q(is_superuser=True) | Q(groups__name='moderator')).order_by('id')


# Moderator views
class BaseModeratorView(BaseGroupRequiredMixin):
    group_required = 'moderator'


# Miner views
class BaseMinerView(BaseGroupRequiredMixin):
    group_required = 'miner'


class MinerRawTextListView(BaseMinerView):
    template_name = 'mine/admin/raw_texts.html'
    queryset = Text.objects.all()