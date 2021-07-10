from django.urls import path

from .views import (
            EbookListCreateAPIView, 
            EbookDetailAPIView, 
            ReviewCreateAPIView,
            ReviewDetailAPIView
            )

urlpatterns = [
    path('/', EbookListCreateAPIView.as_view(), name='ebook_list'),
    path('/<int:pk>', EbookDetailAPIView.as_view(), name='ebook_detail'),
    path('/<int:ebook_pk>/review', ReviewCreateAPIView.as_view(), name='ebook_review'),
    path('/reviews/<int:pk>', ReviewDetailAPIView.as_view(), name='review_list'),
]
