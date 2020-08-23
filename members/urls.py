from django.urls import path
from .views import UserRegisterView, Profile, PasswordsChangeView
# from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('profile/', Profile, name = 'profile'),
    #path('password/', PasswordChangeView.as_view(template_name='registration/change_password.html'), name='password'),
    path('password/', PasswordsChangeView.as_view(), name='password'),
]
