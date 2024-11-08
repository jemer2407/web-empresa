from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Link

# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created')
    # metodo para modificar en el panel admin
    # metodo para poner los campos "key" y "name" de la app social en solo lectura
    def get_readonly_fields(self, request, obj=None):
        # si detecta un usuario en administracion y pertenece al grupo
        # Personal, poner los campos en solo lectura
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')




admin.site.register(Link, LinkAdmin)