from django.urls import path
from .views import HomeView, ProblemDetailView, AddProblemView, UpdateProblemView, DeleteProblemView, StatusView, LikeView, UserPostListView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('problem/<int:pk>', ProblemDetailView.as_view(), name ='problem-detail'),
    path('add_post/',AddProblemView.as_view(), name = 'add_post'),
    path('problem/edit/<int:pk>', UpdateProblemView.as_view(), name ='update_post'),
    path('problem/<int:pk>/remove/', DeleteProblemView.as_view(), name ='delete_post'),
    path('status/<str:cats>/', StatusView, name ='status'),
    path('like/<int:pk>', LikeView, name='like_post'),
]
