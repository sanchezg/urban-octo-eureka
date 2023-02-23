from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from users.factories import UserFactory


class AuthTestCase(TestCase):
    def setUp(self) -> None:
        password = "abcdef102938"

        self.client = APIClient()
        self.user = UserFactory()
        # self.user.set_password(password)
        # self.user.save()
        self.user_data = {"username": self.user.username, "password": password}
        self.login_url = reverse("knox_login")
        self.logout_url = reverse("knox_logout")
        return super().setUp()

    def test_logged_in_user_can_access_auth_views(self):
        response = self.client.post(self.login_url, data=self.user_data, format="json")

        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn("token", response_data)

        token = response_data["token"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        response = self.client.get(reverse("user-list"))
        self.assertEqual(response.status_code, 200)

    def test_logged_out_user_cant_access_auth_views(self):
        self.client.login(**self.user_data)  # login
        self.client.post(self.login_url, data=self.user_data, format="json")  # logout

        response = self.client.get(reverse("user-list"))
        self.assertEqual(response.status_code, 401)

    def test_anon_user_can_access_index(self):
        pass
