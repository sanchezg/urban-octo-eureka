from rest_framework import permissions, viewsets

from .models import Content, Kit, KitContent
from .serializers import ContentSerializer, KitSerializer, KitContentSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
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
