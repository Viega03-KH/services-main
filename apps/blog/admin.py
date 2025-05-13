from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'status')  # Admin panelda ustunlar
    list_filter = ('status', 'publish')  # Filtrlash imkoniyati
    search_fields = ('title_uz', 'title_en', 'content_uz', 'content_en')  # Qidiruv
    prepopulated_fields = {'slug': ('title_en',)}  # Slugni avtomatik yaratish
    fieldsets = (
        ('Asosiy maʼlumotlar', {
            'fields': ('preview',),
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
            'fields': ('publish', 'slug', 'status',),
        }),
    )

    def get_title(self, obj):
        return obj.get_title()
    get_title.short_description = "Title"

