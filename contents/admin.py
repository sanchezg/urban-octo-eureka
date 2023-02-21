from django.contrib import admin
from .models import Content, KitContent, Kit


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "is_free",)
    list_filter = ("user", "is_free")


class KitContentAdmin(admin.TabularInline):
    model = KitContent


@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "created_at", "items_count",)

    inlines = (KitContentAdmin,)

    @admin.display(description="Items")
    def items_count(self, obj):
        return obj.contents.count()


admin.site.register(KitContent)
