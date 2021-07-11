from django.urls import path, include

urlpatterns = [
    path('/profiles', include('api.profiles.urls')),
]
