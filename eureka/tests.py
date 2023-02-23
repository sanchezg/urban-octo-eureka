from unittest import skip

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from users.factories import UserFactory


class AuthTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.login_url = reverse("knox_login")
        self.logout_url = reverse("knox_logout")
        return super().setUp()

    @skip("Too slow to set password")
    def test_logged_in_user_can_access_auth_views(self):
        password = "abcdef102938"
        user = UserFactory(password=password)
        user_data = {"username": user.username, "password": password}

        response = self.client.post(self.login_url, data=user_data, format="json")

        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn("token", response_data)

        token = response_data["token"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        response = self.client.get(reverse("user-list"))
        self.assertEqual(response.status_code, 200)

    @skip("Too slow to set password")
    def test_logged_out_user_cant_access_auth_views(self):
        password = "abcdef102938"
        user = UserFactory(password=password)
        user_data = {"username": user.username, "password": password}
        self.client.login(**user_data)  # login
        self.client.post(self.login_url, data=user_data, format="json")  # logout

        response = self.client.get(reverse("user-list"))
        self.assertEqual(response.status_code, 401)

    def test_anon_user_can_access_index(self):
        self.client.credentials()  # Override existing ones (if there are some)
        response = self.client.get(reverse("contents:index"))

        self.assertEqual(response.status_code, 200)
