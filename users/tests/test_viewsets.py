from rest_framework import status
from users.tests.test_setup import TestSetUp


class TestUserViewSet(TestSetUp):

    def test_list_admin(self):
        response = self.client.get(
            '/users/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_admin(self):
        response = self.client.post(
            '/users/', 
            {
                'email': "dummy@example.com",
                'password': 'password123'
            },
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_admin(self):
        response = self.client.delete(
            '/users/1/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_set_quota(self):
        response = self.client.put(
            '/users/1/quota/', 
            {
                'quota': 2,
            },
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Invalid cases

    def test_create_admin_invalid(self):
        response = self.client.post(
            '/users/', 
            {
                'email': "123",
                'password': 'password123'
            },
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_admin_invalid(self):
        response = self.client.delete(
            '/users/2/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # No admin cases

    def test_list(self):
        self.no_admin_mode()
        response = self.client.get(
            '/users/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create(self):
        self.no_admin_mode()
        response = self.client.post(
            '/users/', 
            {
                'email': "dummy@example.com",
                'password': 'password123'
            },
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete(self):
        self.no_admin_mode()
        response = self.client.delete(
            '/users/1/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

