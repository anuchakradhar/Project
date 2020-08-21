from django.urls import path
from .views import UserRegisterView, Profile

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('profile/', Profile, name = 'profile'),
    # path('edit_profile/', UserEditView.as_view(), name = 'edit_profile'),

]
