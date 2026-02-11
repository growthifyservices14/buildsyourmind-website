from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'list', views.WorkshopViewSet)
router.register(r'bookings', views.WorkshopBookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
