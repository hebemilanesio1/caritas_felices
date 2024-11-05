from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from appprueba import views

urlpatterns = [
    path('crear-campana/', views.crear_campana, name='crear_campana'),
    path('campanas-activas/', views.campanas_activas_view, name='campanas_activas'),
]

if settings.DEBUG:  # Solo servir archivos media en modo de desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)