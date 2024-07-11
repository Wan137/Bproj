from django.urls import path
from .views import register, login_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register', register, name='register'),
    path('login', login_user, name='login-user'),
    path('logout', LogoutView.as_view(), name='logout')
]