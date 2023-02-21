from rest_framework import serializers

from .models import Content, Kit, KitContent


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
