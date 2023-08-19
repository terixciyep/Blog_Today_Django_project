from rest_framework.test import APITestCase
from django.urls import reverse



class BlogsPagesTestCase(APITestCase):
    def test_get_main_page(self):
        response = self.client.get(reverse('MainPageSpace:manpage'))
        self.assertEqual(response.status_code, 200)
