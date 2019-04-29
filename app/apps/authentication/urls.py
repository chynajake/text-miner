from django.urls import path

from apps.authentication.views import RegistrationView

app_name = 'authentication'
urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='registration'),
    # TODO activate by email stuff
    # path('signin/', )
]