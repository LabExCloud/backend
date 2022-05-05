from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import LanguageListSerializer, LanguageDemoCodeSerializer
from .models import Language


class LanguageList(APIView):
    def get(self, request, format=None):
        serializer = LanguageListSerializer(Language.objects.all(), many=True)
        return Response(serializer.data)


class LanguageDemoCode(APIView):
    def get(self, request, lang_id, format=None):
        serializer = LanguageDemoCodeSerializer(Language.objects.get(id=lang_id))
        return Response(serializer.data)