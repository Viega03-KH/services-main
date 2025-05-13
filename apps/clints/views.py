from django.shortcuts import render
from rest_framework import viewsets
from .models import Clint
from .serializers import ClintSerializer
# Create your views here.




class ClintViewSet(viewsets.ModelViewSet):
    queryset = Clint.objects.all()
    serializer_class = ClintSerializer