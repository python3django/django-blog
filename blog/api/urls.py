from django.urls import path, include
from . import views


app_name = 'api'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name=views.PostListView.name),
    path('posts/<pk>/', views.PostDetailView.as_view(), name=views.PostDetailView.name),
    path('comments/', views.CommentListView.as_view(), name=views.CommentListView.name),
    path('comments/<pk>/', views.CommentDetailView.as_view(), name=views.CommentDetailView.name), 
]
