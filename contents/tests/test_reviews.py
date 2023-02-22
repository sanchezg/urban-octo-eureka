from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from contents.factories import ContentFactory, ContentReviewFactory
from users.factories import UserFactory

class ContentReviewViewSetTestCase(TestCase):

    BASE_URL = reverse("review-list")

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = UserFactory()
        self.content = ContentFactory()
        return super().setUp()

    def test_user_can_review_content(self):
        self.client.force_authenticate(user=self.user)
        request_data = {
            "user": self.user.pk,
            "content": self.content.pk,
            "review": "great content!",
            "score": 5,
        }

        response = self.client.post(self.BASE_URL, data=request_data, format="json")

        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["user"], self.user.pk)
        self.assertEqual(data["content"], self.content.pk)
        self.assertEqual(data["review"], "great content!")
        self.assertEqual(data["score"], 5)

    def test_publisher_cant_review_own_content(self):
        user = self.content.user
        self.client.force_authenticate(user=user)

        request_data = {
            "user": user.pk,
            "content": self.content.pk,
            "review": "great content!",
            "score": 5,
        }

        response = self.client.post(self.BASE_URL, data=request_data, format="json")

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()[0], "You can't review your own content")


class ContentReviewTestCase(TestCase):

    def test_avg_score_computes_right_score(self):
        content = ContentFactory()

        acc = 0
        for i in range(10):
            score = i+1
            ContentReviewFactory(content=content, score=score)
            acc += score
        avg = acc / 10
        self.assertAlmostEqual(avg, content.score)
