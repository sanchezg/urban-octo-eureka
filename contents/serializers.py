from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import Bookmark, Content, ContentReview, Kit, KitContent


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = (
            "user",
            "name",
            "description",
            "is_free",
        )


class KitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = "__all__"


class KitContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitContent
        fields = "__all__"


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = "__all__"


class ContentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentReview
        fields = "__all__"

    def create(self, validated_data):
        if validated_data["user"] and validated_data["content"]:
            if validated_data["content"].user.pk == validated_data["user"].pk:
                raise serializers.ValidationError(_("You can't review your own content"))
        return super().create(validated_data)
