from django.urls import reverse
from rest_framework.test import APITestCase

from .models import User


class UserViewSetTestCase(APITestCase):
    BASE_URL = reverse("user-list")

    def test_get_all_returns_active_users(self):
        active_user = User(
            username="username1",
            first_name="First",
            last_name="Last",
            password="password1234",
            is_seller=True,
        )
        active_user.save()
        inactive_user = User(
            username="username2",
            first_name="First",
            last_name="Last",
            password="password1234",
            is_active=False,
        )
        inactive_user.save()


        self.client.force_authenticate(user=active_user)
        response = self.client.get(self.BASE_URL, format="json")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["username"], active_user.username)

    def test_get_all_returns_non_test_users(self):
        non_test_user = User(
            username="username1",
            first_name="First",
            last_name="Last",
            password="password1234",
            is_seller=True,
        )
        non_test_user.save()
        test_user = User(
            username="username2",
            first_name="First",
            last_name="Last",
            password="password1234",
            is_test_user=True,
        )
        test_user.save()


        self.client.force_authenticate(user=non_test_user)
        response = self.client.get(self.BASE_URL, format="json")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["username"], non_test_user.username)
