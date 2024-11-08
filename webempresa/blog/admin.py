from django.contrib import admin
from .models import Category, Post


# Register your models here.
# clase para extender las funcionalidades del panel de admin
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title','content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    # creacion de un campo propio en el admin
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = 'Categorias'



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

# Configuración del panel de gestion de administrador
title = "Proyecto Web Empresa"
subtitle = 'Panel de gestión de Posts'
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
