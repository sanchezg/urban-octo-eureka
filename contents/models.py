from django.db import models
from django.conf import settings

UserModel = settings.AUTH_USER_MODEL


class BaseContent(models.Model):
    """A base model class for all related content."""

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, help_text="Seller user that published this content")
    name = models.CharField("Content title", max_length=32, blank=False)
    description = models.TextField("Content description", max_length=256, blank=True)
    is_free = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Image(BaseContent):
    pass


class Video(BaseContent):
    pass


class Document(BaseContent):
    pass


class Kit(models.Model):
    """A kit made from one or more contents"""
    user = models.ForeignKey(UserModel, db_index=True, on_delete=models.CASCADE, help_text="Seller user that published this kit")
    name = models.CharField("Kit title", max_length=32, blank=False)
    description = models.TextField("Kit description", max_length=256, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class KitContent(models.Model):
    """An intermediate table that relates kits and contents"""

    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    image_content = models.ForeignKey(Image, null=True, on_delete=models.CASCADE, blank=True)
    video_content = models.ForeignKey(Video, null=True, on_delete=models.CASCADE, blank=True)
    document_content = models.ForeignKey(Document, null=True, on_delete=models.CASCADE, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.kit}: {self._get_content()} from '{self.kit.user}'"

    def _get_content(self):
        if self.image_content:
            return self.image_content
        elif self.video_content:
            return self.video_content
        elif self.document_content:
            return self.document_content
