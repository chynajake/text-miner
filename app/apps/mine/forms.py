from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from apps.mine.models import Text


class TextForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TextForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-offline-ticket'
        self.helper.form_class = 'OfflineTicket'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', u'Отправить'))

    class Meta:
        model = Text
        fields = '__all__'


