from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .serializers import LabExperimentSerializer, LabQuestionSerializer, LabTestCaseSerializer, LabAnswerSerializer
from .models import LabExperiment, LabQuestion, LabAnswer, LabTestCase
from .permissions import HasAnswerPermission

from classes.serializers import ClassSerializer
from classes.permissions import HasPermission
from classes.models import Class


class LabsList(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request):
        classes = request.user.student.classes.filter(is_lab=True)
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)


class LabsSemList(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request, format=None, **kwargs):
        sem = kwargs.get('sem', request.user.student.semester.sem)
        classes = request.user.student.classes.filter(semester=sem, is_lab=True)
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)


class LabExperimentsList(APIView):
    permission_classes = [IsAuthenticated & HasPermission]
    
    def get(self, request, id, format=None):
        lab_exps = LabExperiment.objects.filter(class_a=id)
        serializer = LabExperimentSerializer(lab_exps, many=True)
        return Response(serializer.data)


class LabExperimentDetail(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request, id, format=None):
        exp = LabExperiment.objects.get(pk=id)
        serializer = LabExperimentSerializer(exp)
        return Response(serializer.data)
    
    def post(self, request, id, format=None):
        try:
            c = Class.objects.get(pk=id)
            self.check_object_permissions(request, c)
            serializer = LabExperimentSerializer(data=request.data)
            print(request.data)
            if(serializer.is_valid(raise_exception=True)):
                e = serializer.save(class_a=c)
                return Response(LabExperimentSerializer(e).data)
            print(serializer.data)
            return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(Class.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id, format=None):
        try:
            e = LabExperiment.objects.get(pk=id)
            self.check_object_permissions(request, e.class_a)
            serializer = LabExperimentSerializer(e, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(LabExperiment.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id, format=None):
        try:
            e = LabExperiment.objects.get(pk=id)
            self.check_object_permissions(request, e.class_a)
            e.delete()
            return Response('deleted', status=status.HTTP_200_OK)
        except(LabExperiment.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class LabQuestionDetail(APIView):
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request, id):
        try:
            q = LabQuestion.objects.get(pk=id)
            serializer = LabQuestionSerializer(q)
            return Response(serializer.data)
        except(LabQuestion.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, id):
        try:
            e = LabExperiment.objects.get(pk=id)
            self.check_object_permissions(request, e.class_a)
            serializer = LabQuestionSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(experiment=e)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except(LabExperiment.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            q = LabQuestion.objects.get(pk=id)
            self.check_object_permissions(request, q.experiment.class_a)
            serializer = LabQuestionSerializer(q, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except(LabQuestion.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            q = LabQuestion.objects.get(pk=id)
            self.check_object_permissions(request, q.experiment.class_a)
            q.delete()
            return Response(status=status.HTTP_200_OK)
        except(LabQuestion.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class LabTestCaseDetail(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [IsAuthenticated & HasPermission]

    def get(self, request, id):
        try:
            t = LabTestCase.objects.get(pk=id)
            serializer = LabTestCaseSerializer(t)
            return Response(serializer.data)
        except(LabTestCase.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, id):
        try:
            q = LabQuestion.objects.get(pk=id)
            self.check_object_permissions(request, q.experiment.class_a)
            serializer = LabTestCaseSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(question=q)
                return Response(serializer.data)
            return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(LabQuestion.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            t = LabTestCase.objects.get(pk=id)
            self.check_object_permissions(request, t.question.experiment.class_a)
            serializer = LabTestCaseSerializer(t, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response('invalid data', status=status.HTTP_400_BAD_REQUEST)
        except(LabTestCase.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            t = LabTestCase.objects.get(pk=id)
            self.check_object_permissions(request, t.question.experiment.class_a)
            t.delete()
            return Response('deleted')
        except(LabTestCase.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class LabAnswerDetail(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [IsAuthenticated & HasAnswerPermission]

    def post(self, request, id):
        try:
            q = LabQuestion.objects.get(pk=id)
            self.check_object_permissions(request, q.experiment.class_a)
            request.data['student'] = request.user.student.id
            request.data['question'] = id
            serializer = LabAnswerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except(LabQuestion.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        except(IntegrityError):
            return Response(
                'answer for this question by this student already exist',
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, id):
        try:
            a = LabAnswer.objects.get(pk=id)
            self.check_object_permissions(request, a.question.experiment.class_a)
            request.data['student'] = request.user.student.id
            request.data['question'] = a.question.id
            serializer = LabAnswerSerializer(a, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except(LabAnswer.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        try:
            a = LabAnswer.objects.get(pk=id)
            self.check_object_permissions(request, a.question.experiment.class_a)
            a.delete()
            return Response('deleted')
        except(LabAnswer.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
    
