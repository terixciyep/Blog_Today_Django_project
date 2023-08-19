from django.urls import path
from . import views

app_name = 'MainPage'

urlpatterns = [
    path('', views.main_page, name='manpage')
]