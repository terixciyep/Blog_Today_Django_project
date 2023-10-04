import datetime

from rest_framework.test import APITestCase
from django.urls import reverse
from blogs.models import Blog, Category
from datetime import date
from users.models import Users

class BlogsPagesTestCase(APITestCase):
    def test_get_main_page(self):
        response = self.client.get(reverse('blogsSpace:mainpage'))
        self.assertEqual(response.status_code, 200)

    def test_get_blogs_pages_and_create_bd_notes_with_Users_and_Blogs(self):
        print(datetime.date.today())
        user = Users.objects.create_user(username='me',password='1a2s3d4f5g', id = 0)
        category = Category.objects.create(name='Здоровье', id=0)
        blog = Blog.objects.create(title='test1',description='des1',content='con1', author_id = 0, category_id = 0)
        blog2 = Blog.objects.create(title='test2',description='des2',content='con2', author_id = 0, category_id = 0)
        blog3 = Blog.objects.create(title='test3',description='des3',content='con3', author_id = 0, category_id = 0)
        allBlogs = Blog.objects.all()
        for blog in allBlogs:
            blog_id = blog.id
            response = self.client.get(reverse(f'blogsSpace:idpage', args=[blog_id]))
            self.assertEqual(response.status_code, 200)