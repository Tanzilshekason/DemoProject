from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adminpanel/', include('adminpanel.urls')),
    path('admin/', admin.site.urls),
    # path('admins/',include('adminpanel.urls')),

]
