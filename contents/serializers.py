from rest_framework import serializers

from .models import Content, Kit, KitContent, Bookmark, ContentReview


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ("user", "name", "description", "is_free",)


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
