from rest_framework import serializers
from .models import Workshop, WorkshopBooking


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'


class WorkshopBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopBooking
        fields = '__all__'
        read_only_fields = ['status']
