
from django.urls import path, include

urlpatterns = [
    path('/jobs', include('api.jobs.urls')),
]
