from django.contrib import admin
from .models import Service

# Register your models here.
# clase para extender las funcionalidades del panel de admin
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'created')




admin.site.register(Service, ServiceAdmin)

# Configuración del panel de gestion de administrador
title = "Proyecto Web Empresa"
subtitle = 'Panel de gestión'
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle