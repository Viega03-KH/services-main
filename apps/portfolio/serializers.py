from rest_framework import serializers
from .models import Portfolio, Category, Technology

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        exclude = ('title_uz', 'title_en', 'title_ru', 'content_uz', 'content_en', 'content_ru')

    def get_title(self, obj):
        return obj.title  

    def get_content(self, obj):
        return obj.content  
