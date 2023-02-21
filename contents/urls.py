from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import index, detail
from .viewsets import ContentViewSet, KitContentViewSet, KitViewSet


app_name = "contents"

router = DefaultRouter()
router.register(r"contents", ContentViewSet)
router.register(r"kitcontents", KitContentViewSet)
router.register(r"kits", KitViewSet)

urlpatterns = [
    path("", index, name="index"),
    path("<int:content_id>/", detail, name="details"),
]
