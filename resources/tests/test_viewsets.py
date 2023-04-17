from unittest import mock
from rest_framework import status
from users.models import Quota
from users.tests.test_setup import TestSetUp


class TestResourcesViewSet(TestSetUp):

    def test_list_admin(self):
        response = self.client.get(
            '/resources/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_admin(self):
        resource_obj = self.client.post(
            '/resources/', 
            {
                'value': "string example"
            },
            headers=self.headers
        )

        response = self.client.get(
            '/resources/1/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_admin(self):
        response = self.client.post(
            '/resources/', 
            {
                'value': "string example"
            },
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_delete_admin(self):
        resource_obj = self.client.post(
            '/resources/', 
            {
                'value': "string example"
            },
            headers=self.headers
        )

        response = self.client.delete(
            '/resources/1/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Admin invalid cases

    def test_delete_invalid_id_admin(self):
        response = self.client.delete(
            '/resources/1/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_admin(self):
        response = self.client.post(
            '/resources/', 
            {
                'incorrect_field': 1
            },
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # No admin cases

    def test_list(self):
        self.no_admin_mode()
        response = self.client.get(
            '/resources/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        self.no_admin_mode()
        resource_obj = self.client.post(
            '/resources/', 
            {
                'value': "string example"
            },
            headers=self.headers
        )

        response = self.client.get(
            '/resources/1/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        self.no_admin_mode()
        response = self.client.post(
            '/resources/', 
            {
                'value': "string example"
            },
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        self.no_admin_mode()
        resource_obj = self.client.post(
            '/resources/', 
            {
                'value': "string example"
            },
            headers=self.headers
        )

        response = self.client.delete(
            '/resources/1/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # No admin invalid cases

    def test_delete_invalid_id(self):
        self.no_admin_mode()
        response = self.client.delete(
            '/resources/9/', 
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def fake_get_max_resources(self):
        return 1

    @mock.patch.object(Quota, "get_max_resources", fake_get_max_resources)
    def test_create_no_quota(self):
        self.no_admin_mode()

        response = self.client.post(
            '/resources/', 
            {
                'value': "string example"
            },
            headers=self.headers
        )
        response = self.client.post(
            '/resources/', 
            {
                'value': "string example"
            },
            headers=self.headers
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

