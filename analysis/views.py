from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from labs.models import LabQuestion, LabAnswer, LabExperiment
from classes.models import Class

from .serializers import ExperimentReportSerializer, ExperimentReport

# Create your views here.


class ReportView(APIView):
    def get(self, request, cid, sid):
        try:
            es = LabExperiment.objects.filter(class_a=cid)
        except(LabAnswer.DoesNotExist):
            return Response('class not found', status.HTTP_404_NOT_FOUND)
        
        exps = []
        for e in es:
            qa = []
            count = 0
            ontime = 0
            for q in e.questions.all():
                try:
                    qa.append((q, q.answers.get(student=sid)))
                    count += 1
                    if e.due_date >= q.answers.get(student=sid).modified:
                        ontime += 1
                except(LabAnswer.DoesNotExist):
                    continue
            exps.append((e, qa, len(e.questions.all()), ontime))

        
        # for e in exps:
        #     print('\n\nExp: ', e[0].exp_name)
        #     for (q, a) in e[1]:
        #         eff = a.execution_time / q.stdExecTime
        #         if eff < 1:
        #             print(q, "code_efficiency = good")
        #         else:
        #             print(q, "code_efficiency = poor")
        
        exrs = []

        for (e, qa, total, ontime) in exps:
            obj = ExperimentReport(e, len(qa), ontime)
            exrs.append(obj)
        
        serializer = ExperimentReportSerializer(exrs, many=True)
        
        return Response(serializer.data)