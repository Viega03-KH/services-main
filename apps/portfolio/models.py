from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # Har bir til uchun sarlavha (title)
    title_uz = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_ru = models.CharField(max_length=200, blank=True, null=True)

    # Har bir til uchun kontent (content)
    content_uz = models.TextField(blank=True, null=True)
    content_en = models.TextField(blank=True, null=True)
    content_ru = models.TextField(blank=True, null=True)

    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    preview = models.ImageField(upload_to='portfolios/', null=False, blank=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='portfolios', null=True)
    technologies = models.ManyToManyField(Technology, related_name='portfolios', blank=True)
    website = models.CharField(max_length=500, blank=True, null=True)

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Our Portfolio'
        verbose_name_plural = 'Our Portfolios'

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
        return reverse('portfolio_detail', args=[self.slug])

    def __str__(self):
        return self.get_title()
