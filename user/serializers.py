from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Profile
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'get_image',
            'semester',
            'rollno',
            'phone',
        )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'profile'
        )