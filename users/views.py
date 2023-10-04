from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
import django_filters.rest_framework as RSfilers
from users.forms import UserRegistrationFrom, AuthUserForm, ChangeUserForm
from django.contrib import auth
from blogs.models import Blog
from users.models import Users
from users.serializer import UserSerializer
from rest_framework import generics

def profile(request):
    if request.method == 'POST':
        form = ChangeUserForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('usersSpace:mainpage'))
    else:
        form = ChangeUserForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request, 'users/profile.html', context)
def registerion(request):
    error = ''
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('MainPageSpace:manpage'))
        else:
            error = form.errors
    else:
        form = UserRegistrationFrom()
    context = {
        'form': form,
        'error':error
    }
    return render(request, 'users/registration.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthUserForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('usersSpace:mainpage'))
    else:
        form = AuthUserForm()
    context = {
        'form':form
    }
    return render(request, 'users/login.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('MainPage:manpage'))

def myBlogs(request):
    blogs = Blog.objects.filter(author=request.user)
    context = {
        'blogs':blogs
    }
    return render(request, 'users/myBlogs.html', context)

class UsersViewSet(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [RSfilers.DjangoFilterBackend]
    filterset_fields = ['id', 'username', 'email', 'password','is_staff']