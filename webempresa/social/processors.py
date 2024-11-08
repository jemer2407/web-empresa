from .models import Link
"""
funcion para crear un diccionario con todas las redes sociales que nuestro cliente
haya creado desde el panel de administrador.
Creamos un diccionario cuya clave sera el campo key y el valor el enlace de la red social
Este diccionario es el que devolvemos como contexto para extenderlo y usuarlo 
en cualquier template de todo el proyecto
"""
 
 
def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx









# funcion para extender el contexto
# lo que se pretende es poder utilizar el diccionario ctx en cada una de las templates
# a esto se le llama extender el contexto

"""
def ctx_dict(request):
    ctx = {'test':'hola'}
    return ctx
"""

