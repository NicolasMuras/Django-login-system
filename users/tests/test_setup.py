from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class TestSetUp(APITestCase):

    def setUp(self):
        # Creates an User object, procced login and retrieve a JWT token used to make API requests.
  
        self.login_url = '/login/'

        self.user = User.objects.create_superuser(
            username="nico@example.com",
            email="nico@example.com",
            password='password123'
        )
        response = self.client.post(
            self.login_url,
            {
                'email': "nico@example.com",
                'password': 'password123'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        self.headers = {"Authorization": "Token {}".format(self.token)}

        return super().setUp()

    def no_admin_mode(self):
        self.user = User.objects.create_user(
            username="common_user@example.com",
            email="common_user@example.com",
            password='password123'
        )

        response = self.client.post(
            self.login_url,
            {
                'email': "common_user@example.com",
                'password': 'password123'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        self.headers = {"Authorization": "Token {}".format(self.token)}