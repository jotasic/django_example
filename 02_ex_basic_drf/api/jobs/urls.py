
from django.urls import path

from .views import JobOfferCreateListAPIView, JobOfferDetailAPIView

urlpatterns = [
    path('/', JobOfferCreateListAPIView.as_view(), name='job_offer_list'),
    path('/<int:pk>', JobOfferDetailAPIView.as_view(), name='job_offer_detail'),
    
]
