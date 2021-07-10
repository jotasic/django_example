from django.urls import path, include

urlpatterns = [
    path('/quotes', include('api.quotes.urls')),
]
