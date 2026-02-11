from django.contrib import admin
from .models import Enquiry, SchoolInquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'enquiry_type', 'email', 'phone', 'status', 'created_at']
    list_filter = ['enquiry_type', 'status']
    search_fields = ['name', 'email', 'company_name']

@admin.register(SchoolInquiry)
class SchoolInquiryAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'contact_person', 'email', 'city', 'status', 'created_at']
    list_filter = ['status', 'city']
    search_fields = ['school_name', 'contact_person', 'email']
