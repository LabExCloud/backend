from rest_framework import serializers

from .models import Student, Teacher, User
    

class StudentSerializer(serializers.ModelSerializer):
    semester = serializers.SerializerMethodField()
    dept_name = serializers.SerializerMethodField()
    dept_code = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()
    stream = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = (
            'dept_name',
            'dept_code',
            'semester',
            'rollno',
            'year',
            'stream'
        )
        depth = 2
    
    def get_semester(self, obj):
        return obj.semester.sem
    
    def get_dept_code(self, obj):
        return obj.department.dept_code
    
    def get_dept_name(self, obj):
        return obj.department.dept_name

    def get_year(self, obj):
        return obj.batch.year

    def get_stream(self, obj):
        return obj.batch.stream


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ()


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'is_superuser',
            'is_staff',
            'phone',
            'get_image',
            'profile',
        )
    
    def get_profile(self, user):
        if ((not user.is_superuser) & (not user.is_staff)):
            student = Student.objects.get(user=user)
            return StudentSerializer(student, read_only=True).data
        elif ((not user.is_superuser) & (user.is_staff)):
            teacher = Teacher.objects.get(user=user)
            return TeacherSerializer(teacher, read_only=True).data