import datetime

import django_filters
from django.shortcuts import render, HttpResponseRedirect
from blogs.models import Blog, Comment, Category
from django.urls import reverse
from blogs.forms import BlogCreateForm, CommentForm
from rest_framework.generics import ListCreateAPIView
from django.core.paginator import Paginator



def BlogsPage(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    menu = Category.objects.all()
    categories = Category.objects.all()
    context = {
        'blogs':page_obj,
        'menu':menu,
        'categories':categories
    }
    return render(request, 'blogs/blogsPage.html', context)

def BlogsFiltredPage(request,pk):

    blogs = Blog.objects.filter(category=pk)
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    context = {
        'blogs':page_obj,
        'categories':categories
    }
    return render(request, 'blogs/blogsPage.html', context)

def BlogPage(request, blog_id):
    error = ''
    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.filter(blod_id=blog_id)
    commentForm = CommentForm(initial={'comment_author': request.user, 'blod_id': blog})
    if request.method == 'POST':
        commentForm = CommentForm(data=request.POST)
        if commentForm.is_valid():
            commentForm.save()
        else:
            error = commentForm.errors
    if not blog:
        return HttpResponseRedirect(reverse('blogsSpace:mainpage'))
    context = {
        'blog_id': blog_id,
        'blog' : blog,
        'comments':comments,
        'form':commentForm,
        'error':error
    }
    return render(request, 'blogs/blog.html', context)

def createBlog(request):
    error = ''
    user = request.user
    if request.method == 'POST':
        form = BlogCreateForm(data=request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return HttpResponseRedirect(reverse('usersSpace:mainpage'))
        else:
            error = form.errors
    else:
        form = BlogCreateForm(initial={'date_posted': datetime.datetime.today(), 'author':user})

    context = {
        'form': form,
        'error':error
    }
    return render(request, 'blogs/blogCreate.html', context)

def deleteComment(request, comment_id, blog_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.comment_author:
        comment.delete()
        return HttpResponseRedirect(reverse('blogsSpace:idpage', args=[blog_id]))
    else:
        return HttpResponseRedirect(reverse('blogsSpace:mainpage'))

def allBlogsForUserPage(request):
    BlogForUser = Blog.objects.filter(author=request.user).order_by('-date_posted')
    context = {
        'blogs':BlogForUser
    }
    return render(request, 'blogs/AllUserBlogs.html', context)
