from rest_framework import serializers
from .models import Subject, Teacher, TuitionApplication, TeacherRegistration


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class TeacherListSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'photo', 'qualification', 'experience_years',
                  'subjects', 'city', 'area', 'rating', 'is_featured']


class TeacherDetailSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        exclude = ['email', 'phone']


class TuitionApplicationSerializer(serializers.ModelSerializer):
    subject_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = TuitionApplication
        fields = ['id', 'parent_name', 'email', 'phone', 'student_name', 'student_class',
                  'subject_ids', 'city', 'area', 'state', 'preferred_time', 'message']

    def create(self, validated_data):
        subject_ids = validated_data.pop('subject_ids', [])
        application = TuitionApplication.objects.create(**validated_data)
        application.subjects.set(subject_ids)
        return application


class TeacherRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherRegistration
        fields = ['full_name', 'email', 'phone', 'qualification', 'experience_years',
                  'subjects', 'city', 'area', 'state', 'resume', 'message']
