from django.shortcuts import render

# Create your views here.

def home(request):

    title = 'Inicio'
    
    return render(request, 'core/home.html', {
        'title': title
    })


def about(request):

    title = 'Historia'

    return render(request, 'core/about.html', {
        'title': title
    })


def store(request):
    title = 'Visítanos'
    return render(request, 'core/store.html', {
        'title': title
    })


