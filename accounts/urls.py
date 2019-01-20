from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', TemplateView.as_view(template_name='moviepoll/index.html')),
    path('login/', LoginView.as_view(template_name='accounts/login.html')),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html')),
]