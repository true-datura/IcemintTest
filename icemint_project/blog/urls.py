from django.urls import path

from .views import (
    UsersListView,
    PostCreateView,
    PostDetailView,
    PostsListView,
    PostUpdateView
)

app_name = 'blog'
urlpatterns = [
    path('users/', UsersListView.as_view(), name='users-list'),
    path('users/<int:user_id>/', PostsListView.as_view(), name='posts-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('create/', PostCreateView.as_view(), name='post-create')
]
