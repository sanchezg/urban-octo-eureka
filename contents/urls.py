from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import detail, index
from .viewsets import (
    BookmarkViewSet,
    ContentReviewViewSet,
    ContentViewSet,
    KitContentViewSet,
    KitViewSet,
)

app_name = "contents"

router = DefaultRouter()
router.register(r"contents", ContentViewSet)
router.register(r"kitcontents", KitContentViewSet)
router.register(r"kits", KitViewSet)
router.register(r"bookmarks", BookmarkViewSet, basename="bookmark")
router.register(r"reviews", ContentReviewViewSet, basename="review")

urlpatterns = [
    path("", index, name="index"),
    path("<int:content_id>/", detail, name="details"),
]
