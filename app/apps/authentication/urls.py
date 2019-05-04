from django.urls import path

from apps.authentication.views import RegistrationView, SignInView, ExitView

app_name = 'authentication'
urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
    # TODO activate by email stuff
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', ExitView.as_view(), name='signout'),
]