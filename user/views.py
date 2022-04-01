from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer, UserSerializer


class ProfileDetail(APIView):
    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def get_object(self, username):
        try:
            user = User.objects.filter(username=username)[0]
            return user
        except User.DoesNotExist:
            raise Http404


# class ProfileDetail(APIView):
#     def get(self, request, username, format=None):
#         profile = self.get_object(username)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)
    
#     def get_object(self, username):
#         try:
#             user = User.objects.filter(username=username)[0]
#             return user
#             # return Profile.objects.filter(user=user.id)[0]
#         except User.DoesNotExist:
#             raise Http404