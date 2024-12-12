from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsOwnerOrAdmin(BasePermission):
    """
    Allows access to only the owner of the object or admin.
    """
    def has_object_permission(self, request, view, obj):
        # Admins can access any object
        if request.user.is_staff:
            return True
        # The owner can access their own objects
        return obj.user == request.user


class IsAuthenticatedUser(BasePermission):
    """
    Allows access only to authenticated users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsGuest(BasePermission):
    """
    Allows access only to unauthenticated users (guests).
    """
    def has_permission(self, request, view):
        return not request.user.is_authenticated
 