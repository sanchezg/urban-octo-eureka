from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from contents.factories import ContentFactory
from contents.models import Content
from users.factories import UserFactory
from users.models import User


class ContentsViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        return super().setUp()

    def test_index_get_five_newest_contents(self):
        contents_index = reverse("contents:index")

        response = self.client.get(contents_index)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"No contents are available.", response.content)

        # user = UserFactory()
        contents = ContentFactory.create_batch(6)

        response = self.client.get(contents_index)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"These are the last five contents uploaded:", response.content)
        # TODO: check the five items returned are the last ones


class ContentsModelTestCase(TestCase):
    def test_user_consumer_cant_create_content(self):

        user = UserFactory()
        with self.assertRaises(ValidationError) as exc:
            Content.objects.create(user=user, name=f"Title", description=".")
        self.assertIn(
            "Only consumer users can't create content. Please switch to a publisher account.", exc.exception.message
        )
