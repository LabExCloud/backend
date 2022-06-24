import csv
from io import StringIO

from django.db.utils import IntegrityError
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Student, Teacher, User
from .serializers import LightStudentUserSerializer, UserSerializer
from .permissions import IsTeacher, OwnProfilePermission

from base.models import Semester, Batch


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

class CreateStudentsCSV(APIView):
    permission_classes = (IsAuthenticated, IsTeacher, )
    def post(self, request):
        file = request.FILES['file'].read().decode('utf-8')
        reader = csv.DictReader(StringIO(file), delimiter=',')
        count = 0
        department = Teacher.objects.get(user=request.user).department
        for row in reader:
            try:
                user = User(
                    username=row.get('username'),
                    first_name=row.get('firstname'),
                    middle_name=row.get('middlename'),
                    last_name=row.get('lastname'),
                    email=row.get('email'),
                    phone=row.get('phone'),
                    user_type=User.UserType.STUDENT,
                    is_superuser=False,
                    is_staff=False,
                )
                user.set_password(row.get('password'))
                user.save()
            except(IntegrityError):
                continue
            student = Student(
                user=user,
                rollno=int(row.get('rollno')),
                department=department,
                semester=Semester.objects.get(sem=int(row.get('semester'))),
                batch=Batch.objects.get(Q(stream=row.get('stream')) & Q(year=int(row.get('year'))))
            )
            student.save()
            count += 1
        return Response('{0} students added'.format(count))