from rest_framework import permissions


class IsAdminOrIsSelf(permissions.BasePermission):
    def has_permission(self, request, view):
        return any(
            [
                request.user.is_superuser,
                request.user.is_staff,
                request.user.pk == int(request.parser_context["kwargs"].get("pk")),
            ]
        )
