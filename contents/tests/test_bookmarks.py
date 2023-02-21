from django.urls import reverse
from rest_framework.test import APITestCase

from contents.models import Bookmark
from users.factories import UserFactory, SellerUserFactory
from contents.factories import BookmarkFactory, ContentFactory


class BookmarkViewSetTestCase(APITestCase):
    BASE_URL = reverse("bookmark-list")

    def test_bookmarks_list_returns_user_bookmarks(self):
        user1 = SellerUserFactory()
        user2 = UserFactory()

        content1 = ContentFactory(user=user1)
        BookmarkFactory(user=user1, content=content1)
        BookmarkFactory(user=user2, content=content1)

        self.client.force_authenticate(user=user1)
        response = self.client.get(self.BASE_URL, format="json")

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(len(data["results"]), 1)
        self.assertEqual(data["results"][0]["user"], user1.pk)

    def test_user_can_bookmark_a_content(self):
        user1 = UserFactory()

        content1 = ContentFactory()

        self.client.force_authenticate(user=user1)
        post_data = {
            "user": user1.pk,
            "content": content1.pk
        }
        response = self.client.post(self.BASE_URL, data=post_data, format="json")
        self.assertEqual(response.status_code, 201)

        data = response.json()
        self.assertEqual(data["user"], user1.pk)
        self.assertEqual(data["content"], content1.pk)

        bk = Bookmark.objects.get(user=user1, content=content1)
        self.assertIsNotNone(bk)
