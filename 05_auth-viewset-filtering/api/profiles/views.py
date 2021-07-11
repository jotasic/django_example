from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from .models import Profile, ProfileStatus
from .serializers import ProfileAvatarSerializer, ProfileSerializer, ProfileStatusSerializer
from api.permissions import IsOwnProfileOrReadOnly, IsOwnOrReadOnly

class ProfileViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet): 
    queryset           = Profile.objects.all()
    serializer_class   = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]

class ProfileStatusViewSet(ModelViewSet):
    serializer_class   = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnOrReadOnly]

    def get_queryset(self):
        queryset = ProfileStatus.objects.select_related('user_profile', 'user_profile__user').all()
        username = self.request.query_params.get('username', None)

        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)

class ProfileAvatarAPIView(generics.UpdateAPIView):
    serializer_class   = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object
        
