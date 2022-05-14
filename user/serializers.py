from rest_framework import serializers

from classes.models import Class

from .models import Student, Teacher, User
    

class StudentSerializer(serializers.ModelSerializer):
    semester = serializers.SerializerMethodField()
    semesters = serializers.SerializerMethodField()
    dept_name = serializers.SerializerMethodField()
    dept_code = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()
    stream = serializers.SerializerMethodField()

    class Meta:
        model = Student
        exclude = (
            'department',
            'user'
        )
    
    def get_semester(self, obj):
        return obj.semester.sem
    
    def get_semesters(self, obj):
        semesters = [i.semester.sem for i in obj.classes.all()]
        return list(set(semesters))
    
    def get_dept_code(self, obj):
        return obj.department.dept_code
    
    def get_dept_name(self, obj):
        return obj.department.dept_name

    def get_year(self, obj):
        return obj.batch.year

    def get_stream(self, obj):
        return obj.batch.stream


class TeacherSerializer(serializers.ModelSerializer):
    dept_name = serializers.SerializerMethodField()
    dept_code = serializers.SerializerMethodField()
    classes = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), many=True)

    class Meta:
        model = Teacher
        exclude = (
            'department',
            'user'
        )
    
    def get_dept_code(self, obj):
        return obj.department.dept_code
    
    def get_dept_name(self, obj):
        return obj.department.dept_name


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