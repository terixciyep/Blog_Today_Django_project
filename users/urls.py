from django.urls import path
from . import views

app_name = 'Users'

urlpatterns = [
    path('', views.profile, name='mainpage'),
    path('/registration', views.registerion, name='registration'),
    path('/login', views.login, name='login'),
    path('/logout', views.logout, name='logout'),
    path('/myblogs', views.myBlogs, name='myblogs')
]