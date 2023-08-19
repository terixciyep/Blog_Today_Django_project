from django.urls import path
from . import views

app_name = 'Blogs'

urlpatterns = [
    path('', views.feedbackPage, name='form'),
]