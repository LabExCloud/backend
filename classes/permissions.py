from rest_framework import permissions
from user.models import User, Teacher


class HasPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.user_type == User.UserType.TEACHER) | (request.method in permissions.SAFE_METHODS)
    
    def has_object_permission(self, request, view, obj):
        teacher = Teacher.objects.get(user=request.user)
        teachers = obj.teachers.all()
        return teacher in teachers
    

class HasOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.user_type == User.UserType.TEACHER) | (request.method in permissions.SAFE_METHODS)
    
    def has_object_permission(self, request, view, obj):
        teacher = Teacher.objects.get(user=request.user)
        return teacher == obj.owner