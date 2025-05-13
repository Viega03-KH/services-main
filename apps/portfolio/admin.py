from django.contrib import admin
from .models import Portfolio, Technology, Category

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)  

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'publish', 'status') 
    list_filter = ('status', 'publish')  
    search_fields = ('title_uz', 'title_en', 'title_ru', 'content_uz', 'content_en', 'content_ru')  
    prepopulated_fields = {'slug': ('title_en',)}  
    filter_horizontal = ('technologies',)  
    fieldsets = (
        ('Asosiy maʼlumotlar', {
            'fields': ('category', 'preview',),
        }),
        ('Title (Sarlavha)', {
            'fields': ('title_uz', 'title_en', 'title_ru'),
            'classes': ('collapse',)  # Bosilganda ochiladigan
        }),
        ('UZ Content', {
            'fields': ('content_uz',),
            'classes': ('collapse',)  
        }),
        ('EN Content', {
            'fields': ('content_en',),
            'classes': ('collapse',)  
        }),
        ('RU Content', {
            'fields': ('content_ru',),
            'classes': ('collapse',)  
        }),
        ('Qo‘shimcha', {
            'fields': ('technologies', 'website', 'publish', 'slug', 'status',),
        }),
    )
