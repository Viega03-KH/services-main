from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify 
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title_uz = models.CharField(max_length=200)  
    title_en = models.CharField(max_length=200)  
    title_ru = models.CharField(max_length=200)  
    slug = models.SlugField(max_length=200, unique_for_date='publish') 
    preview = models.ImageField(upload_to='post/', null = False, blank = False)
    content_uz = RichTextUploadingField(null=True, config_name="default", )  
    content_en = RichTextUploadingField(null=True, config_name="default", )  
    content_ru = RichTextUploadingField(null=True, config_name="default", )  
    publish = models.DateTimeField(default=timezone.now)  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')  

    class Meta:
        ordering = ('-publish',)  
        verbose_name = 'Our Post'
        verbose_name_plural = 'Our Posts'
    def save(self, *args, **kwargs):
        """Slug yaratishda default til (Inglizcha) dan foydalanish"""
        if not self.slug and self.title_en:
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    
    def get_title(self, lang="en"):
        """Til bo‘yicha mos sarlavhani qaytarish"""
        return getattr(self, f"title_{lang}", self.title_en) or self.title_en

    def get_content(self, lang="en"):
        """Til bo‘yicha mos kontentni qaytarish"""
        return getattr(self, f"content_{lang}", self.content_en) or self.content_en

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def __str__(self):
        return self.get_title()
