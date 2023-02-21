from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

UserModel = settings.AUTH_USER_MODEL


class ContentType:

    VIDEO = "video"
    DOCUMENT = "document"
    IMAGE = "image"

    CHOICES = [
        (VIDEO, _("Video")),
        (DOCUMENT, _("Document")),
        (IMAGE, _("Image")),
    ]


class Content(models.Model):
    """A base model class for all related content."""

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, help_text="Seller user that published this content")
    name = models.CharField("Content title", max_length=32, blank=False)
    description = models.TextField("Content description", max_length=256, blank=True)
    is_free = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # type
    content_type = models.CharField(choices=ContentType.CHOICES, default=ContentType.VIDEO, max_length=12, blank=False)

    def __str__(self) -> str:
        return f"{self.name} ({self.content_type})"

    def save(self, **kwargs) -> None:
        if not self.user.is_seller:
            raise ValidationError(_("Only consumer users can't create content. Please switch to a publisher account."))
        return super().save(**kwargs)


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

    kit = models.ForeignKey(Kit, on_delete=models.CASCADE, related_name="contents")
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="kits_included")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.kit}: {self.content} from '{self.kit.user}'"


class ContentTagColor:
    GREY = "grey"
    RED = "red"
    BLUE = "blue"
    YELLOW = "yellow"
    GREEN = "green"

    CHOICES = [
        (GREY, _("Grey")),
        (RED, _("Red")),
        (BLUE, _("Blue")),
        (YELLOW, _("Yellow")),
        (GREEN, _("Green")),
    ]


class ContentTag(models.Model):
    name = models.CharField(max_length=32, blank=False, unique=True)
    color = models.CharField(max_length=32, choices=ContentTagColor.CHOICES, default=ContentTagColor.GREY)
    contents = models.ManyToManyField(Content, related_name="tags", blank=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.color})"


class Bookmark(models.Model):
    content = models.ForeignKey(Content, related_name="bookmarks", on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, related_name="bookmarks", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [
            ["content", "user"],
        ]

    def __str__(self) -> str:
        return f"Bookmark: '{self.content}' from '{self.user}'"
