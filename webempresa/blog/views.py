from django.shortcuts import render, get_object_or_404
from .models import Category, Post

# Create your views here.

def blog(request):
    title = 'Blog'

    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {
        'title': title,
        'posts': posts
    })

def category(request, category_id):
    title = 'Categorias'
    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id)

    return render(request, 'blog/category.html', {
        'title': title,
        'category': category
    })
