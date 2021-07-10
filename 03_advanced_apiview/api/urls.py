from django.urls import path, include

urlpatterns = [
    path('/ebooks', include('api.ebooks.urls')),
]
