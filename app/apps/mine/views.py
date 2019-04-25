from django.views.generic import CreateView

from apps.mine.forms import TextForm


class TextCreateView(CreateView):
    form_class = TextForm
    template_name = 'mine/text_create.html'
