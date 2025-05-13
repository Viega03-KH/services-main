from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status='published')  # Faqat published holatdagilarni olish
    serializer_class = PostSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'uz')  # Default til: 'uz'
        queryset = Post.objects.filter(status='published')

        # Har bir Portfolio uchun kerakli til bo‘yicha `title` va `content`ni olish
        for post in queryset:
            post.title = getattr(post, f'title_{lang}', post.title_uz)
            post.content = getattr(post, f'content_{lang}', post.content_uz)

        return queryset

