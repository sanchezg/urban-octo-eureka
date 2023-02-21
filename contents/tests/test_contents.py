from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.urls import reverse

from contents.models import Content
from users.models import User


class ContentsViewTestCase(TestCase):

    def test_index_get_five_newest_contents(self):
        client = Client()
        contents_index = reverse("contents:index")

        response = client.get(contents_index)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"No contents are available.", response.content)

        user = User(
            username="username",
            first_name="First",
            last_name="Last",
            password="password1234",
            is_seller=True,
        )
        user.save()

        for i in range(6):
            Content.objects.create(user=user, name=f"Title{i}", description=".")  # pk starts in 1

        response = client.get(contents_index)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"These are the last five contents uploaded:", response.content)
        for i in range(1, 6):
            self.assertIn(f"Title{i}".encode(), response.content)


class ContentsModelTestCase(TestCase):

    def test_user_consumer_cant_create_content(self):

        user = User(
            username="username",
            first_name="First",
            last_name="Last",
            password="password1234",
            is_seller=False,
        )
        user.save()

        with self.assertRaises(ValidationError) as exc:
            Content.objects.create(user=user, name=f"Title", description=".")
        self.assertIn("Only consumer users can't create content. Please switch to a publisher account.", exc.exception.message)
