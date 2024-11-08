from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    title = 'Servicios'

    services = Service.objects.all()
    return render(request, 'services/services.html', {
        'title': title,
        'services': services
    })
