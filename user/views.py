from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer
from .permissions import OwnProfilePermission


class ProfileDetail(APIView):
    permission_classes = (IsAuthenticated, OwnProfilePermission,)
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
