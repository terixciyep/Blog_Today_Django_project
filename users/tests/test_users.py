from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.models import Users

class UserPagesTestCase(APITestCase):
    def test_get_profile_page(self):
        user = get_user_model()
        user = Users.objects.create_user(username='me',password='1a2s3d4f5g', id = 0)
        self.client.force_login(user)
        response = self.client.get(reverse('usersSpace:mainpage'))
        self.assertEqual(response.status_code, 200)

    def test_reg_profile_page(self):
        data = {
            'first_name': 'Артем',
            'last_name': 'Коробов',
            'username': 'artemich123',
            'email': 'artyom.korobov@list.ru',
            'password1': '1a2s3d4f5g!!@@',
            'password2': '1a2s3d4f5g!!@@',
        }
        response = self.client.post(reverse('usersSpace:registration'), data)
        user_exists = Users.objects.filter(username='artemich123').exists()
        self.assertTrue(user_exists)

    def test_login_page(self):
        user = Users.objects.create_user(username='me',password='1a2s3d4f5g', id = 0)
        self.client.login(username='me',password='1a2s3d4f5g')
        response = self.client.get(reverse('usersSpace:login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        user = Users.objects.create_user(username='me',password='1a2s3d4f5g', id = 0)
        self.client.login(username='me',password='1a2s3d4f5g')
        response = self.client.get(reverse('usersSpace:login'))
        self.assertEqual(response.status_code, 200)
        response = self.client.logout()

