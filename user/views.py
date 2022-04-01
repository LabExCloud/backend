from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import ProfileSerializer, UserSerializer

from .permissions import OwnProfilePermission


class ProfileDetail(APIView):
    permission_classes = (IsAuthenticated, OwnProfilePermission,)
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
