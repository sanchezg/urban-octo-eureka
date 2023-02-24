from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .factories import UserFactory


class UserViewSetTestCase(TestCase):
    BASE_URL = reverse("user-list")

    def setUp(self) -> None:
        self.client = APIClient()
        return super().setUp()

    def test_get_all_returns_active_users(self):
        active_user = UserFactory()
        inactive_user = UserFactory()
        inactive_user.is_active = False
        inactive_user.save()

        self.client.force_authenticate(user=active_user)
        response = self.client.get(self.BASE_URL, format="json")

        self.assertEqual(response.status_code, 200)

        data = response.json()["results"]
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["username"], active_user.username)

    def test_get_all_returns_non_test_users(self):
        non_test_user = UserFactory()
        test_user = UserFactory()
        test_user.is_test_user = True
        test_user.save()

        self.client.force_authenticate(user=non_test_user)
        response = self.client.get(self.BASE_URL, format="json")

        self.assertEqual(response.status_code, 200)

        data = response.json()["results"]
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["username"], non_test_user.username)

    def test_set_is_seller(self):
        user = UserFactory()
        self.client.force_authenticate(user=user)
        url = reverse("user-set-as-seller", kwargs={"pk": user.pk})

        response = self.client.post(url, format="json")
        self.assertEqual(response.status_code, 200)

        user.refresh_from_db()
        self.assertTrue(user.is_seller)
