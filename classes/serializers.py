from rest_framework import serializers

from user.models import User, Teacher
from user.serializers import LightUserSerializer

from .models import Class

from base.models import Subject, Department, Semester, Batch
from base.serializers import SubjectSerializer, DepartmentSerializer, SemesterSerializer, BatchSerializer


class ClassSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    department = Department()
    semester = Semester()
    subject = Subject()
    batch = Batch()
    owner = Teacher()
    teachers = serializers.ListField()
    is_lab = serializers.BooleanField(default=False)

    def to_representation(self, instance):
        teachers = [i.user for i in instance.teachers.all()]

        return {
            'id': instance.id,
            'department': DepartmentSerializer(instance.department).data,
            'semester': SemesterSerializer(instance.semester).data,
            'subject': SubjectSerializer(instance.subject).data,
            'batch': BatchSerializer(instance.batch).data,
            'owner': LightUserSerializer(instance.owner.user).data,
            'teachers': LightUserSerializer(teachers, many=True).data,
            'is_lab': instance.is_lab
        }

    def to_internal_value(self, data):
        user = self.context['request'].user
        owner = Teacher.objects.get(pk=user.teacher.id)
        tids = data.get('teachers', [])
        if user.teacher.id not in tids:
            tids.append(user.teacher.id)
        teachers = [Teacher.objects.get(pk=i) for i in tids]
        try:
            dept = Department.objects.get(pk=data.get('department'))
            sem = Semester.objects.get(pk=data.get('semester'))
            sub = Subject.objects.get(pk=data.get('subject'))
            batch = Batch.objects.get(pk=data.get('batch'))
        except(Department.DoesNotExist):
            raise serializers.ValidationError({'department': 'does not exist'})
        except(Semester.DoesNotExist):
            raise serializers.ValidationError({'semester': 'does not exist'})
        except(Subject.DoesNotExist):
            raise serializers.ValidationError({'subject': 'does not exist'})
        except(Batch.DoesNotExist):
            raise serializers.ValidationError({'batch': 'does not exist'})
        
        return {
            'id': data.get('id'),
            'department': dept,
            'semester': sem,
            'subject': sub,
            'batch': batch,
            'owner': owner,
            'teachers': teachers,
            'is_lab': data.get('is_lab', False)
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

    # teachers = serializers.SerializerMethodField()
    # owner = serializers.SerializerMethodField()

    # class Meta:
    #     validators = []
    #     model = Class
    #     fields = (
    #         'id',
    #         'department',
    #         'semester',
    #         'subject',
    #         'batch',
    #         'owner',
    #         'teachers',
    #         'is_lab',
    #     )
    #     depth = 1
    
    # def get_owner(self, obj):
    #     serializer = LightUserSerializer(obj.owner.user)
    #     return serializer.data
    
    # def get_teachers(self, obj):
    #     teachers = [i.user for i in obj.teachers.all()]
    #     serializer = LightUserSerializer(teachers, many=True)
    #     return serializer.data