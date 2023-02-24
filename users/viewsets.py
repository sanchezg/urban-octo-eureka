from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .permissions import IsAdminOrIsSelf
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True, is_test_user=False)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"], permission_classes=[IsAdminOrIsSelf])
    def set_as_seller(self, request, pk=None):  # TODO: Add permission to filter this view
        """
        Use this view for additional actions like sending an email or notification
        """
        user = self.get_object()
        if user.is_seller:
            raise exceptions.ValidationError(_("User is already set as seller"))
        user.set_is_seller()
        return Response(self.serializer_class(user).data)
