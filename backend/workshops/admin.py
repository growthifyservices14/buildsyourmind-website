from django.contrib import admin
from .models import Workshop, WorkshopBooking

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['title', 'workshop_type', 'target_audience', 'duration', 'is_active']
    list_filter = ['workshop_type', 'target_audience', 'is_active']

@admin.register(WorkshopBooking)
class WorkshopBookingAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'contact_person', 'phone', 'workshop_type', 'preferred_date', 'status', 'created_at']
    list_filter = ['status', 'workshop_type']
    search_fields = ['school_name', 'contact_person', 'email']
