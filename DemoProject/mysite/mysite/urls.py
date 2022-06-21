from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adminpanel/', include('adminpanel.urls')),
    path('admin/', admin.site.urls),
    path('',include('eshopper.urls')),
    path('OAuth', include('social_django.urls', namespace='social')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
