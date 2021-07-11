import json

from django.contrib.auth.models import User
from django.http import response
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse

from .models import Profile
from .serializers import ProfileSerializer

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {'username' : 'testcase', 'email' :'test@localhost.app', 
                'password1': 'some_strong_psw', 'password2': 'some_strong_psw'}
        response = self.client.post('/api/rest-auth/registration/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):
    list_url = reverse('profile-list')

    def setUp(self):
        self.user = User.objects.create(username='admin', password='some-strong-password')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse('profile-detail', kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'admin')