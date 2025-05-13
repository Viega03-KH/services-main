from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


class Ourservises(models.Model):
    # Har bir til uchun sarlavha (title)
    title_uz = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_ru = models.CharField(max_length=200, blank=True, null=True)

    # Har bir til uchun kontent (content)
    content_uz = models.TextField(blank=True, null=True)
    content_en = models.TextField(blank=True, null=True)
    content_ru = models.TextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Our Servises'
        verbose_name_plural = 'Our Servises'


    def get_title(self, lang="en"):
        """Til bo‘yicha mos sarlavhani qaytarish"""
        return getattr(self, f"title_{lang}", self.title_en) or self.title_en

    def get_content(self, lang="en"):
        """Til bo‘yicha mos kontentni qaytarish"""
        return getattr(self, f"content_{lang}", self.content_en) or self.content_en


    def __str__(self):
        return self.get_title()