from django.urls import path

from .views import index, detail

app_name = "contents"
urlpatterns = [
    path("", index, name="index"),
    path("<int:content_id>/", detail, name="details")
]
