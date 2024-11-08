from django.urls import path
from services import views
from django.conf import settings



urlpatterns = [
    path('services/', views.services, name='services'),    
]

# Ruta imagenes para que se muestren en el panel de administrador cuando estemos en desarrollo (settings.DEBUG == True)

if settings.DEBUG:
    from django.conf.urls.static import static
    # variables MEDIA_URL Y MEDIA_ROOT las tenemos que declarar en el settings del proyecto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)