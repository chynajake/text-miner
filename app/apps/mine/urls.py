from django.urls import path

from apps.mine.views import TextCreateView

urlpatterns = [
    path('text/create/', TextCreateView.as_view(), name='text-create'),
]