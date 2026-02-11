from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'testimonials', views.TestimonialViewSet)
router.register(r'gallery', views.GalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('settings/', views.site_settings),
    path('newsletter/', views.newsletter_subscribe),
]
