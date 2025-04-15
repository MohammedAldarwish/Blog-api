from rest_framework.routers import DefaultRouter
from .views import CommentListView
from django.urls import path

urlpatterns = [
    path('blogs/<int:blog_id>/comments/', CommentListView.as_view(), name='blog-comments'),
]