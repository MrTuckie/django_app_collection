from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class Test_home(TestCase):

    @classmethod
    def setUp(cls):
        cls.client = Client()

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home/index.html')