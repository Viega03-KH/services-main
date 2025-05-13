from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger schema yaratish
schema_view = get_schema_view(
    openapi.Info(
        title="HardSoft Tech API",
        default_version='v1',
        description="HardSoft Tech loyihasi uchun API hujjatlari",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),

    # API yo‘llari
    path('api/', include([
        path('', include('blog.urls')),
        path('', include('clints.urls')),
        path('', include('ourservises.urls')),
        path('', include('portfolio.urls')),
    ])),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# Statik va media fayllar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
