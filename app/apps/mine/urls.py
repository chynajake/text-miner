from django.urls import path

from apps.mine.views import TextCreateView

app_name = 'mine'
urlpatterns = [
    path('text/create/', TextCreateView.as_view(), name='text-create'),
]