from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')   # se crea automaticamente la primera vez que se crea el registro
    updated = models.DateTimeField(auto_now=True, verbose_name='Editado el')   # se actualiza cada vez que se edita un campo del registro

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = CKEditor5Field(verbose_name='Contenido', config_name='extends')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)    # CASCADE - si borramos un autor se borran todas sus Posts
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name = 'get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')   # se crea automaticamente la primera vez que se crea el registro
    updated = models.DateTimeField(auto_now=True, verbose_name='Editado el')   # se actualiza cada vez que se edita un campo del registro

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']
    
    def __str__(self):
        return self.title