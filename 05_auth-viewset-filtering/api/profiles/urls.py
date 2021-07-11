from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet, ProfileStatusViewSet, ProfileAvatarAPIView

router = DefaultRouter()
router.register(r'status', ProfileStatusViewSet, basename='status')
router.register(r'', ProfileViewSet)

urlpatterns = [
    path('/', include(router.urls)),
    path('/avatar', ProfileAvatarAPIView.as_view(), name='avatar_update')
]
