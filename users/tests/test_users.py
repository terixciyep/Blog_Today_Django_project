import os
import django
from django.urls import reverse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Structure.settings")
django.setup()

from rest_framework import test, status
from users.models import Users


class UsersTestCate(test.APITestCase):
    user_data = {
        'first_name': 'artem',
        'last_name': 'korobov',
        'username': 'again',
        'email': 'artyom.korobov@list.ru',
        'password1': 'securepassword',
        'password2': 'securepassword',
    }
    def test_registration_view(self):
        response = self.client.post(reverse('usersSpace:registration'), self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('MainPageSpace:manpage'))
        self.assertEqual(Users.objects.filter(username='again').exists(), True)
        user = Users.objects.get(username='again')
        self.assertEqual(user.username, 'again')
        self.assertEqual(user.email, 'artyom.korobov@list.ru')
    def test_login(self):
        user = Users.objects.create_user(username='testuser', password='securepassword')
        login_data = {
            'username': 'testuser',
            'password': 'securepassword'
        }
        response = self.client.post(reverse('usersSpace:login'), data=login_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('usersSpace:mainpage'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)
    def test_logout(self):
        user = Users.objects.create_user(username='testuser', password='securepassword')
        login_data = {
            'username': 'testuser',
            'password': 'securepassword'
        }
        response = self.client.post(reverse('usersSpace:login'), data=login_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('usersSpace:mainpage'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        response = self.client.get(reverse('usersSpace:logout'), response)
        self.assertTrue(response.wsgi_request.user.is_authenticated is not True)

    def test_profile(self):
        user = Users.objects.create_user(username='testuser', password='securepassword')
        login_data = {
            'username': 'testuser',
            'password': 'securepassword'
        }
        response = self.client.post(reverse('usersSpace:login'), data=login_data)
        new_login_data = {
            'username': 'testuser2',
            'password': 'securepassword'
        }
        response = self.client.post(reverse('usersSpace:mainpage'), data=new_login_data)
        self.assertEqual(response.wsgi_request.user.username,'testuser2')