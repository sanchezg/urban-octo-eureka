from django.contrib import admin
from .models import Content, KitContent, Kit, ContentTag, Bookmark


class ContentTagInline(admin.TabularInline):
    model = ContentTag.contents.through

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "is_free",)
    list_filter = ("user", "is_free")

    inlines = (ContentTagInline,)


class KitContentAdmin(admin.TabularInline):
    model = KitContent


@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "created_at", "items_count",)

    inlines = (KitContentAdmin,)

    @admin.display(description="Items")
    def items_count(self, obj):
        return obj.contents.count()


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("user", "content",)
    list_filter = ("user", "content",)


admin.site.register(KitContent)
admin.site.register(ContentTag)
