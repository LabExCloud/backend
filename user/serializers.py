from rest_framework import serializers

from base.serializers import DepartmentSerializer

from classes.models import Class

from .models import Student, Teacher, User
    

class StudentSerializer(serializers.ModelSerializer):
    semester = serializers.SerializerMethodField()
    semesters = serializers.SerializerMethodField()
    department = DepartmentSerializer(read_only=True)
    year = serializers.SerializerMethodField()
    stream = serializers.SerializerMethodField()

    class Meta:
        model = Student
        exclude = (
            'user',
        )
    
    def get_semester(self, obj):
        return obj.semester.sem
    
    def get_semesters(self, obj):
        semesters = [i.semester.sem for i in obj.classes.all()]
        return list(set(semesters))
    
    def get_year(self, obj):
        return obj.batch.year

    def get_stream(self, obj):
        return obj.batch.stream


class TeacherSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    classes = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), many=True)

    class Meta:
        model = Teacher
        exclude = (
            'user',
        )


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'phone',
            'image',
            'profile',
            'user_type',
        )
    
    def get_profile(self, user):
        if user.user_type == User.UserType.STUDENT:
            student = Student.objects.get(user=user)
            return StudentSerializer(student, read_only=True).data
        elif user.user_type == User.UserType.TEACHER:
            teacher = Teacher.objects.get(user=user)
            return TeacherSerializer(teacher, read_only=True).data


class LightUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
        )