from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import LabExam, LabExamAnswer, LabExamQuestion, LabExamTestCase
from .serializers import LabExamAnswerSerializer, LabExamQuestionSerializer, LabExamSerializer, LabExamTestCaseSerializer

from classes.serializers import ClassSerializer
from classes.permissions import HasPermission
from classes.models import Class
from labs.permissions import HasAnswerPermission

from user.models import Student, User

# Create your views here.


class LabExamsList(APIView):
    permission_classes = [IsAuthenticated & HasPermission]
    
    def get(self, request, id, format=None):
        lab_exps = LabExam.objects.filter(class_a=id)
        serializer = LabExamSerializer(lab_exps, many=True)
        return Response(serializer.data)


class LabExamDetail(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request, id, format=None):
        exp = LabExam.objects.get(pk=id)
        serializer = LabExamSerializer(exp)
        return Response(serializer.data)
    
    def post(self, request, id, format=None):
        try:
            c = Class.objects.get(pk=id)
            self.check_object_permissions(request, c)
            serializer = LabExamSerializer(data=request.data)
            if(serializer.is_valid(raise_exception=True)):
                e = serializer.save(class_a=c)
                return Response(LabExamSerializer(e).data)
            return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(Class.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id, format=None):
        try:
            e = LabExam.objects.get(pk=id)
            self.check_object_permissions(request, e.class_a)
            serializer = LabExamSerializer(e, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(LabExam.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id, format=None):
        try:
            e = LabExam.objects.get(pk=id)
            self.check_object_permissions(request, e.class_a)
            e.delete()
            return Response('deleted', status=status.HTTP_200_OK)
        except(LabExam.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class LabExamQuestionDetail(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request, id):
        try:
            q = LabExamQuestion.objects.get(pk=id)
            serializer = LabExamQuestionSerializer(q)
            return Response(serializer.data)
        except(LabExamQuestion.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, id):
        try:
            e = LabExam.objects.get(pk=id)
            self.check_object_permissions(request, e.class_a)
            serializer = LabExamQuestionSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(exam=e)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except(LabExam.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            q = LabExamQuestion.objects.get(pk=id)
            self.check_object_permissions(request, q.exam.class_a)
            serializer = LabExamQuestionSerializer(q, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except(LabExamQuestion.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            q = LabExamQuestion.objects.get(pk=id)
            self.check_object_permissions(request, q.exam.class_a)
            q.delete()
            return Response(status=status.HTTP_200_OK)
        except(LabExamQuestion.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class LabExamTestCaseDetail(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request, id):
        try:
            t = LabExamTestCase.objects.get(pk=id)
            serializer = LabExamTestCaseSerializer(t)
            return Response(serializer.data)
        except(LabExamTestCase.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, id):
        try:
            q = LabExamQuestion.objects.get(pk=id)
            self.check_object_permissions(request, q.exam.class_a)
            serializer = LabExamTestCaseSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(question=q)
                return Response(serializer.data)
            return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(LabExamQuestion.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            t = LabExamTestCase.objects.get(pk=id)
            self.check_object_permissions(request, t.question.exam.class_a)
            serializer = LabExamTestCaseSerializer(t, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(LabExamTestCase.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            t = LabExamTestCase.objects.get(pk=id)
            self.check_object_permissions(request, t.question.exam.class_a)
            t.delete()
            return Response('deleted')
        except(LabExamTestCase.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class LabExamAnswerStudentQuestion(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, id):
        try:
            student = Student.objects.get(user=request.user)
            answer = LabExamQuestion.objects.get(pk=id).answers.get(student=student)
            serializer = LabExamAnswerSerializer(answer)
            return Response(serializer.data)
        except(LabExamQuestion.DoesNotExist):
            return Response('question does not exist', status=status.HTTP_404_NOT_FOUND)


class LabExamAnswerDetail(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [IsAuthenticated & HasAnswerPermission]

    def post(self, request, id):
        try:
            q = LabExamQuestion.objects.get(pk=id)
            self.check_object_permissions(request, q.exam.class_a)
            request.data['student'] = request.user.student.id
            request.data['question'] = id
            serializer = LabExamAnswerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except(LabExamQuestion.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        except(IntegrityError):
            return Response(
                'answer for this question by this student already exist',
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, id):
        try:
            a = LabExamAnswer.objects.get(pk=id)
            self.check_object_permissions(request, a.question.exam.class_a)
            request.data['student'] = request.user.student.id
            request.data['question'] = a.question.id
            serializer = LabExamAnswerSerializer(a, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except(LabExamAnswer.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            a = LabExamAnswer.objects.get(pk=id)
            self.check_object_permissions(request, a.question.exam.class_a)
            a.delete()
            return Response('deleted')
        except(LabExamAnswer.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
