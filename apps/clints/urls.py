from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClintViewSet  # ViewSet klassingizni import qilish

# DRF router yaratish
router = DefaultRouter()
router.register(r'clints', ClintViewSet, basename='clints')

urlpatterns = [
    path('', include(router.urls)),  # Barcha ViewSet marshrutlarini qo‘shish
]
