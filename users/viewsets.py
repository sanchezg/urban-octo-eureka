from rest_framework import viewsets, permissions

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)  # TODO: add an "is_test" to user model
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
