from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # Django Admin site
    path('admin/', admin.site.urls),

    # API documentation routes (using drf-spectacular)
    # The raw OpenAPI schema in YAML/JSON
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI: You can interact with your API here
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc UI: A clean documentation view
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # API endpoints for the 'books' app (or your app name)
    path('api/', include('books.urls')),
]
