from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='john', password='pass')

    def test_can_list_profile(self):
        john = User.objects.get(username='john')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        john = User.objects.create_user(username='john', password='pass')
        jane = User.objects.create_user(username='janet', password='pass')

        def test_can_retrieve_profile_using_valid_id(self):
            response = self.client.get('/profiles/1/')
            self.assertEqual(response.data['owner'], 'john')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_cant_retrieve_profile_using_invalid_id(self):
            response = self.client.get('/profiles/999/')
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
