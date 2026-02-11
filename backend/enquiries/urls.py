from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'enquiry', views.EnquiryViewSet)
router.register(r'school-inquiry', views.SchoolInquiryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
