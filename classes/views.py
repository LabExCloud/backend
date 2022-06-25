from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from user.models import Student, User
from user.permissions import IsTeacher
from user.serializers import LightStudentUserSerializer

from .serializers import ClassSerializer
from .models import Class
from .permissions import HasPermission, HasOwnerPermission


class ClassList(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request):
        try:
            classes = []
            if request.user.user_type == User.UserType.STUDENT:
                classes = request.user.student.classes.all()
            elif request.user.user_type == User.UserType.TEACHER:
                classes = request.user.teacher.classes.all()
            else:
                return Response('user does not have classes', status=status.HTTP_404_NOT_FOUND)
            serializer = ClassSerializer(classes, many=True)
            return Response(serializer.data)
        except(Class.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class ClassDetail(APIView):
    permission_classes = [IsAuthenticated & HasOwnerPermission]

    def get(self, request, id):
        try:
            c = Class.objects.get(pk=id)
            serializer = ClassSerializer(c)
            return Response(serializer.data)
        except(Class.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        try:
            serializer = ClassSerializer(data=request.data, context={'user': request.user})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(IntegrityError):
            return Response('class not unique', status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            c = Class.objects.get(pk=id)
            self.check_object_permissions(request, c)
            serializer = ClassSerializer(c, data=request.data, context={'user': request.user})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(IntegrityError):
            return Response('class not unique', status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            c = Class.objects.get(pk=id)
            self.check_object_permissions(request, c)
            c.delete()
            return Response('deleted')
        except(IntegrityError):
            return Response('class not unique', status=status.HTTP_400_BAD_REQUEST)



class StudentListClass(APIView):
    permission_classes = (IsAuthenticated, IsTeacher, )
    def get(self, request, id):
        try:
            c = Class.objects.get(pk=id)
            students = [i.user for i in c.students.all()]
            serializer = LightStudentUserSerializer(students, many=True)
            return Response(serializer.data)
        except(Class.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class AddRemoveStudentClass(APIView):
    permission_classes = (IsAuthenticated, IsTeacher, )
    def post(slef, request, c_id, s_id):
        try:
            student = Student.objects.get(pk=s_id)
            c = Class.objects.get(pk=c_id)
            classes = list(student.classes.all())
            if(c not in classes):
                classes.append(c)
            student.classes.set(classes)
            student.save()
            return Response('added')
        except(Class.DoesNotExist):
            return Response('class does not exist', status=status.HTTP_404_NOT_FOUND)
        except(Student.DoesNotExist):
            return Response('student class does not exist', status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, c_id, s_id):
        try:
            student = Student.objects.get(pk=s_id)
            c = Class.objects.get(pk=c_id)
            classes = list(student.classes.all())
            if(c in classes):
                classes.remove(c)
            student.classes.set(classes)
            student.save()
            return Response('removed')
        except(Class.DoesNotExist):
            return Response('class does not exist', status=status.HTTP_404_NOT_FOUND)
        except(Student.DoesNotExist):
            return Response('student class does not exist', status=status.HTTP_404_NOT_FOUND)

class AddStudentClassCsv(APIView):
    permission_classes = (IsAuthenticated, IsTeacher, )
    def post(self, request, c_id):
        try:
            c = Class.objects.get(pk=c_id)
        except(Class.DoesNotExist):
            return Response('class does not exist', status=status.HTTP_404_NOT_FOUND)
        
        upload_file = request.FILES['file']
        students = upload_file.read().splitlines()
        students = [str(i, 'UTF-8') for i in students]
        err = []
        s = []
        for i in students:
            try:
                student = Student.objects.get(user__username=i)
                s.append(student)
            except(Student.DoesNotExist):
                err.append('{0}: student does not exist'.format(i))
        
        if err == []:
            count = 0
            for st in s:
                classes = list(st.classes.all())
                if(c not in classes):
                    classes.append(c)
                    st.classes.set(classes)
                    st.save()
                    count += 1
            return Response('{0} students added'.format(count))
        else:
            return Response(', '.join(err), status=status.HTTP_404_NOT_FOUND)
