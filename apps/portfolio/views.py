from rest_framework import viewsets
from .models import Portfolio, Category, Technology
from .serializers import PortfolioSerializer, CategorySerializer, TechnologySerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.filter(status='published')  # Faqat published holatdagilarni olish
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'uz')  # Default til: 'uz'
        queryset = Portfolio.objects.filter(status='published')

        # Har bir Portfolio uchun kerakli til bo‘yicha `title` va `content`ni olish
        for portfolio in queryset:
            portfolio.title = getattr(portfolio, f'title_{lang}', portfolio.title_uz)
            portfolio.content = getattr(portfolio, f'content_{lang}', portfolio.content_uz)

        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
