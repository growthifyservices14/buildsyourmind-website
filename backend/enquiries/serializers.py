from rest_framework import serializers
from .models import Enquiry, SchoolInquiry


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ['enquiry_type', 'name', 'email', 'phone', 'company_name', 'city', 'state', 'message']


class SchoolInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolInquiry
        fields = ['school_name', 'contact_person', 'designation', 'email', 'phone',
                  'city', 'state', 'number_of_students', 'interested_in', 'message']
