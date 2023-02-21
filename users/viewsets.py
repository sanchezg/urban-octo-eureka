from rest_framework import viewsets, permissions

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True, is_test_user=False)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
