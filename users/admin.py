from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserCustomAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "full_name",
        "is_seller",
        "is_active",
    )
    list_filter = (
        "is_seller",
        "is_active",
    )

    fieldsets = UserAdmin.fieldsets + ((_("App fields"), {"fields": ("is_seller",)}),)

    @admin.display(description="Full name")
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()


admin.site.register(User, UserCustomAdmin)
