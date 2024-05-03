from django.test import TestCase
from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')

    def test_user_register_login(self):
        url = reverse('users:register')
        data = {
            'email': 'test1@test.ru',
            'password': 'Someasypswrd'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)
        self.assertEqual(response.json().get('email'), 'test1@test.ru')

        url = reverse('users:token_obtain_pair')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
