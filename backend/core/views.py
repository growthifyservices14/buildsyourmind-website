from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SiteSettings, Testimonial, GalleryImage, Newsletter
from .serializers import SiteSettingsSerializer, TestimonialSerializer, GalleryImageSerializer, NewsletterSerializer


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer
    filterset_fields = ['role']


class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalleryImage.objects.filter(is_active=True)
    serializer_class = GalleryImageSerializer
    filterset_fields = ['category']


@api_view(['GET'])
def site_settings(request):
    settings = SiteSettings.objects.first()
    if settings:
        return Response(SiteSettingsSerializer(settings).data)
    return Response({})


@api_view(['POST'])
def newsletter_subscribe(request):
    serializer = NewsletterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Successfully subscribed!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
