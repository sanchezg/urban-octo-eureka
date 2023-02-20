from django.contrib import admin
from .models import Content, KitContent, Kit


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "is_free",)
    list_filter = ("user", "is_free")

admin.site.register(Kit)
admin.site.register(KitContent)
