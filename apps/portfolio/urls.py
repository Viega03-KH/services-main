from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet, CategoryViewSet, TechnologyViewSet

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'technologies', TechnologyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
