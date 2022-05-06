from rest_framework import permissions
from user.models import User, Teacher

class HasAnswerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.user_type == User.UserType.TEACHER) | (obj in request.user.student.classes.all())
