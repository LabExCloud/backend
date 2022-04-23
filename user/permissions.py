from rest_framework import permissions
class OwnProfilePermission(permissions.BasePermission):
    """
    Object-level permission to only allow accessing his own profile
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user

