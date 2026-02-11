from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import Workshop, WorkshopBooking
from .serializers import WorkshopSerializer, WorkshopBookingSerializer


class WorkshopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Workshop.objects.filter(is_active=True)
    serializer_class = WorkshopSerializer
    filterset_fields = ['workshop_type', 'target_audience']


class WorkshopBookingViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = WorkshopBooking.objects.all()
    serializer_class = WorkshopBookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Workshop booking submitted successfully!', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )
