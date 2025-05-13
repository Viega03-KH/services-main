from django.contrib import admin
from .models import Ourservises

@admin.register(Ourservises)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_en',)  # Admin panelda ustunlar
    fieldsets = (
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
        })
    )

    def get_title(self, obj):
        return obj.get_title()
    get_title.short_description = "Title"

