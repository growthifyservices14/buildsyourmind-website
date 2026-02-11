from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import Enquiry, SchoolInquiry
from .serializers import EnquirySerializer, SchoolInquirySerializer


class EnquiryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Thank you for your enquiry! We will get back to you soon.'},
            status=status.HTTP_201_CREATED
        )


class SchoolInquiryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = SchoolInquiry.objects.all()
    serializer_class = SchoolInquirySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Thank you for your interest! Our team will contact you soon.'},
            status=status.HTTP_201_CREATED
        )
