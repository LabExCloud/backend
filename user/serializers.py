from rest_framework import serializers

from .models import Student, Teacher, User
    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'semester',
            'rollno',
        )
        depth = 2


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            'semester',
            'rollno',
        )


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
            'is_superuser',
            'is_staff',
            'phone',
            'get_image',
        )
    
    def get_profile(self, user):
        if ((not user.is_superuser) & (not user.is_staff)):
            student = Student.objects.get(user=user)
            return StudentSerializer(student, read_only=True).data
        elif ((not user.is_superuser) & (user.is_staff)):
            teacher = Teacher.objects.get(user=user)
            return TeacherSerializer(teacher, read_only=True).data