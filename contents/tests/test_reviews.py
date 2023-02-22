from django.test import TestCase
from rest_framework.test import APIClient

from contents.factories import ContentFactory, ContentReviewFactory

class ContentReviewViewSetTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        return super().setUp()

    def test_user_can_review_content(self):
        pass

    def test_publisher_cant_review_own_content(self):
        pass


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
