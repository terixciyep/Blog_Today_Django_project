from django.shortcuts import render, HttpResponse
from blogs.models import Blog, Category


def main_page(request):
    a = Blog.objects.all()[:5]
    categories = Category.objects.all()
    context = {
        'a' : a,
        'categories':categories
    }
    return render(request, 'MainPage/Main.html',context)

