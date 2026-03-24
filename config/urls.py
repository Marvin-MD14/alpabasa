"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Dito papasok ang lahat ng routes mula sa 'webapp' app mo
    path('', include('webapp.urls')), 
]

# SETUP PARA SA MEDIA AT STATIC FILES (Para sa images at videos)
# Ito ay gagana habang naka DEBUG=True ka sa settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Karagdagang safety check para sa static files sa development
urlpatterns += staticfiles_urlpatterns()