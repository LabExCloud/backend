from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Student, User
from .serializers import LightStudentUserSerializer, UserSerializer
from .permissions import IsTeacher, OwnProfilePermission


class ProfileDetail(APIView):
    permission_classes = (IsAuthenticated, OwnProfilePermission,)
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class StudentList(APIView):
    permission_classes = (IsAuthenticated, IsTeacher, )
    def get(self, request):
        students = User.objects.filter(user_type=User.UserType.STUDENT)
        serializer = LightStudentUserSerializer(students, many=True)
        return Response(serializer.data)