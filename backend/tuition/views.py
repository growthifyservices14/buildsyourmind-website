from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import Subject, Teacher, TuitionApplication, TeacherRegistration
from .serializers import (SubjectSerializer, TeacherListSerializer, TeacherDetailSerializer,
                          TuitionApplicationSerializer, TeacherRegistrationSerializer)


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.filter(is_active=True)
    serializer_class = SubjectSerializer


class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teacher.objects.filter(status='active')
    filterset_fields = ['city', 'subjects']
    search_fields = ['full_name', 'city', 'area']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeacherDetailSerializer
        return TeacherListSerializer


class TuitionApplicationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = TuitionApplication.objects.all()
    serializer_class = TuitionApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Tuition application submitted successfully! We will contact you shortly.'},
            status=status.HTTP_201_CREATED
        )


class TeacherRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = TeacherRegistration.objects.all()
    serializer_class = TeacherRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Teacher registration submitted successfully! We will verify and contact you.'},
            status=status.HTTP_201_CREATED
        )
