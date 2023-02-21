from django.urls import reverse
from rest_framework.test import APITestCase

from contents.models import Content, Bookmark
from users.models import User


class BookmarkViewSetTestCase(APITestCase):
    BASE_URL = reverse("bookmark-list")

    def test_bookmarks_list_returns_user_bookmarks(self):
        user1 = User(
            username="username1",
            first_name="First",
            last_name="Last",
            password="password1234",
            is_seller=True,
        )
        user1.save()
        user2 = User(
            username="username2",
            first_name="First",
            last_name="Last",
            password="password1234",
        )
        user2.save()

        content1 = Content(name="C1", description=".", user=user1)
        content1.save()
        
        Bookmark.objects.create(user=user1, content=content1)
        Bookmark.objects.create(user=user2, content=content1)

        self.client.force_authenticate(user=user1)
        response = self.client.get(self.BASE_URL, format="json")

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(len(data["results"]), 1)
        self.assertEqual(data["results"][0]["user"], user1.pk)
