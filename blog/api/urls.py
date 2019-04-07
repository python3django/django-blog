from django.urls import path, include
from . import views 


urlpatterns = [
    path('posts/', views.PostListView.as_view(), name=views.PostListView.name),
    path('posts/<pk>/', views.PostDetailView.as_view(), name=views.PostDetailView.name),
    path('comments/', views.CommentListView.as_view(), name=views.CommentListView.name),
    path('comments/<pk>/', views.CommentDetailView.as_view(), name=views.CommentDetailView.name),
    path('users/', views.UserListView.as_view(), name=views.UserListView.name),
    path('users/<pk>/', views.UserDetailView.as_view(), name=views.UserDetailView.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name), 
]
