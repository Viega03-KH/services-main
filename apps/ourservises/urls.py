from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OurservisesViewSet  # ✅ To‘g‘ri: ViewSet klassini import qilish

# DRF router yaratish
router = DefaultRouter()
router.register(r'ourservices', OurservisesViewSet, basename='ourservices')  # ✅ ViewSet nomini to‘g‘ri qo‘shish

urlpatterns = [
    path('', include(router.urls)),  # ✅ Routerdagi barcha URLlarni qo‘shish
]
