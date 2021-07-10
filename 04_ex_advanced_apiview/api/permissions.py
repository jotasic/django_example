from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return object.author == request.user