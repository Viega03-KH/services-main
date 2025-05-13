from rest_framework import serializers
from .models import Clint


class ClintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clint
        fields = [ 'preview', ]

