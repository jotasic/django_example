from django.urls import path

from .views import QuoteListCreateAPIView, QuoteDetailAPIView

urlpatterns = [
    path('/', QuoteListCreateAPIView.as_view(), name='quote_list'),
    path('/<int:pk>', QuoteDetailAPIView.as_view(), name='quote_detail'),
]
