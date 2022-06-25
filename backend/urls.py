from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('user.urls')),
    path('api/v1/', include('resources.urls')),
    path('api/v1/', include('labs.urls')),
    path('api/v1/', include('labexam.urls')),
    path('api/v1/', include('classes.urls')),
    path('api/v1/', include('editor.urls')),
    path('api/v1/', include('base.urls')),
    path('api/v1/', include('analysis.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
