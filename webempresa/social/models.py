from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name='Nombre clave', max_length=100, unique=True)
    name = models.CharField(verbose_name='Red social', max_length=200)
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')   # se crea automaticamente la primera vez que se crea el registro
    updated = models.DateTimeField(auto_now=True, verbose_name='Editado el')   # se actualiza cada vez que se edita un campo del registro

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name']
    
    def __str__(self):
        return self.name