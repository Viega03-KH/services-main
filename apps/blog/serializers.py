from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    class Meta:
        model = Post
        exclude = ('title_uz', 'title_en', 'title_ru', 'content_uz', 'content_en', 'content_ru')

    def get_title(self, obj):
        return obj.title  

    def get_content(self, obj):
        return obj.content  
