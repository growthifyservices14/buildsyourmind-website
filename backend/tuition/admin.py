from django.contrib import admin
from .models import Subject, Teacher, TuitionApplication, TeacherRegistration

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'city', 'experience_years', 'rating', 'status']
    list_filter = ['status', 'city', 'subjects']
    search_fields = ['full_name', 'email', 'city']

@admin.register(TuitionApplication)
class TuitionApplicationAdmin(admin.ModelAdmin):
    list_display = ['parent_name', 'student_name', 'student_class', 'city', 'assigned_teacher', 'status', 'created_at']
    list_filter = ['status', 'student_class', 'city']
    search_fields = ['parent_name', 'student_name', 'email']

@admin.register(TeacherRegistration)
class TeacherRegistrationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'qualification', 'city', 'status', 'created_at']
    list_filter = ['status', 'city']
    search_fields = ['full_name', 'email']
