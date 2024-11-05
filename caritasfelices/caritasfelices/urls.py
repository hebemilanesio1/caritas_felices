from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appprueba.urls')),  # Incluye las URLs de tu aplicación
]
