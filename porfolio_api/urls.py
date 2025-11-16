from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from porfolio_api import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Portfolio API",
        default_version='v1',
        description="API documentation for my portfolio backend",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your-email@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ReDoc UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Raw JSON/YAML Schema
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)