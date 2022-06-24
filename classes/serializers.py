from rest_framework import serializers

from user.models import Teacher
from user.serializers import LightUserSerializer, LightTeacherUserSerializer

from .models import Class

from base.models import Subject, Department, Semester, Batch
from base.serializers import SubjectSerializer, DepartmentSerializer, SemesterSerializer, BatchSerializer


class ClassSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    semester = serializers.PrimaryKeyRelatedField(queryset=Semester.objects.all())
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    batch = serializers.PrimaryKeyRelatedField(queryset=Batch.objects.all())
    owner = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    teachers = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), many=True)

    class Meta:
        model = Class
        fields = ('__all__')
    
    def to_internal_value(self, data):
        user = self.context['user']
        owner = user.teacher.id
        teachers = data.get('teachers', [])
        if user.teacher.id not in teachers:
            teachers.append(user.teacher.id)

        data['owner'] = owner
        data['teachers'] = teachers

        return super().to_internal_value(data)
        
    def to_representation(self, value):
        return {
            'id': value.id,
            'department': DepartmentSerializer(value.department).data,
            'semester': SemesterSerializer(value.semester).data,
            'subject': SubjectSerializer(value.subject).data,
            'batch': BatchSerializer(value.batch).data,
            'owner': LightUserSerializer(value.owner.user).data,
            'teachers': LightTeacherUserSerializer([i.user for i in value.teachers.all()], many=True).data,
            'is_lab': value.is_lab
        }
    
    def create(self, data):
        teachers = data['teachers']
        data.pop('teachers')
        c = Class.objects.create(**data)
        c.teachers.set(teachers)
        return c
    
    def update(self, c, data):
        c.department = data.get('department', c.department)
        c.semester = data.get('semester', c.semester)
        c.subject = data.get('subject', c.subject)
        c.batch = data.get('batch', c.batch)
        c.owner = data.get('owner', c.owner)
        c.teachers.set(data.get('teachers', c.teachers))
        c.is_lab = data.get('is_lab', c.is_lab)
        c.save()
        return c