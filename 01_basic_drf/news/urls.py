from django.urls import path

from .views  import (
    ArticleListCreateAPIView, ArticleDetailAPIView, 
    journallistListCreateAPIView, journallistDetailAPIView
)
urlpatterns = [
    path('/articles', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('/articles/<int:pk>', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('/journallists', journallistListCreateAPIView.as_view(), name='journallist-list'),
    path('/journallists/<int:pk>', journallistDetailAPIView.as_view(), name='journallist-detail'),
]