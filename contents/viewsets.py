from rest_framework import permissions, viewsets

from .models import Bookmark, Content, ContentReview, Kit, KitContent
from .serializers import (
    BookmarkSerializer,
    ContentReviewSerializer,
    ContentSerializer,
    KitContentSerializer,
    KitSerializer,
)


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.filter(user__is_test_user=False).order_by("-created_at")
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticated]


class KitViewSet(viewsets.ModelViewSet):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer
    permission_classes = [permissions.IsAuthenticated]


class KitContentViewSet(viewsets.ModelViewSet):
    queryset = KitContent.objects.all()
    serializer_class = KitContentSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user).order_by("-created_at")


class ContentReviewViewSet(viewsets.ModelViewSet):
    queryset = ContentReview.objects.all()
    serializer_class = ContentReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
