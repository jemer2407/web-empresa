from django.urls import path
from blog import views
from django.conf import settings



urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/category/<int:category_id>/', views.category, name='category'),
]

# Ruta imagenes para que se muestren en el panel de administrador cuando estemos en desarrollo (settings.DEBUG == True)

if settings.DEBUG:
    from django.conf.urls.static import static
    # variables MEDIA_URL Y MEDIA_ROOT las tenemos que declarar en el settings del proyecto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)