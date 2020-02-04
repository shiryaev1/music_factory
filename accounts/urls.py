from django.contrib.auth.views import LoginView
from django.urls import path
from django.contrib.auth import views as django_auth_views

from accounts.views import RegisterView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', django_auth_views.logout_then_login, name='logout'),
]

