from rest_framework import viewsets
from django.db.models import F
from .models import Ourservises
from .serializers import OurservisesSerializer

class OurservisesViewSet(viewsets.ModelViewSet):
    queryset = Ourservises.objects.all()  # `.all()` chaqirilgan
    serializer_class = OurservisesSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'uz')  # Default til: 'uz'

        return self.queryset.annotate(  # `self.queryset` dan foydalanish
            title=F(f'title_{lang}'),
            content=F(f'content_{lang}')
        )
