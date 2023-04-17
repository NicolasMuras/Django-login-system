from django.test import TestCase
from rest_framework.test import APIRequestFactory
from users.views import Register, Login, Logout, UserToken
from users.models import User


class TestAuthorizationViews(TestCase):

    def test_user_register(self):
        factory = APIRequestFactory()
        request = factory.post('/register/', {
                                            "email": "test_email@gmail.com",
                                            "password": '123456ABCde',
                                            }, format='json')
        view = Register.as_view()
        response = view(request)
        assert 201 == response.status_code

    def test_user_login(self):
        user = User.objects.create(username="test_email@gmail.com", email="test_email@gmail.com")
        user.set_password("123456ABCde")
        user.save()

        factory = APIRequestFactory()
        request = factory.post('/login/', {
                                            "email": "test_email@gmail.com",
                                            "password": '123456ABCde',
                                            }, format='json')
        view = Login.as_view()
        response = view(request)
        assert 200 == response.status_code

    def test_user_logout(self):
        user = User.objects.create(username="test_email@gmail.com", email="test_email@gmail.com")
        user.set_password("123456ABCde")

        user.save()

        factory = APIRequestFactory()
        request = factory.post('/logout/', {
                                            "email": "test_email@gmail.com",
                                            "password": '123456ABCde',
                                            }, format='json')
        view = Login.as_view()
        response = view(request)

        request = factory.post('/logout/?username={}'.format(response.data['user']['email']), HTTP_AUTHORIZATION='Token {}'.format(response.data['token']))
        view = Logout.as_view()
        response = view(request)

        assert 200 == response.status_code

    def test_user_refresh_token(self):
        user = User.objects.create(username="test_email@gmail.com", email="test_email@gmail.com")
        user.set_password("123456ABCde")

        user.save()

        factory = APIRequestFactory()
        request = factory.post('/login/', {
                                            "email": "test_email@gmail.com",
                                            "password": '123456ABCde',
                                            }, format='json')
        view = Login.as_view()
        response = view(request)

        request = factory.get('/refresh-token/?email={}'.format(response.data['user']['email']), HTTP_AUTHORIZATION='Token {}'.format(response.data['token']))
        view = UserToken.as_view()
        response = view(request)

        assert 200 == response.status_code
