from django.urls import path
from . import views

app_name = 'Blogs'

urlpatterns = [
    path('', views.BlogsPage, name='mainpage'),
    path('/<int:blog_id>', views.BlogPage, name='idpage'),
    path('/create', views.createBlog, name='createBlog'),
    path('/filtred/<int:pk>', views.BlogsFiltredPage, name='categoryList'),
    path('/deleteComment/<int:comment_id>/<int:blog_id>', views.deleteComment, name='deleteComment'),
    path('/MyBlogs', views.allBlogsForUserPage, name='AllBlogsForUser')
]