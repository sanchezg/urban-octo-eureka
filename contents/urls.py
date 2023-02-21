from django.urls import path

from .views import index, detail

urlpatterns = [
    path("", index, name="index"),
    path("<int:content_id>/", detail, name="details")
]
