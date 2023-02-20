from django.contrib import admin
from .models import Image, Video, Document, Kit, KitContent


class ContentAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "is_free",)
    list_filter = ("user", "is_free")


admin.site.register(Image, ContentAdmin)
admin.site.register(Video, ContentAdmin)
admin.site.register(Document, ContentAdmin)

admin.site.register(Kit)
admin.site.register(KitContent)
