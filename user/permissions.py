from rest_framework import permissions

from user.models import User
class OwnProfilePermission(permissions.BasePermission):
    """
    Object-level permission to only allow accessing his own profile
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == User.UserType.TEACHER