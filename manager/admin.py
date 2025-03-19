from django.contrib import admin
from .models import *


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "image_preview")  # Display image preview
    list_filter = ("category",)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="border-radius:5px;" />'
        return "-"

    image_preview.allow_tags = True
    image_preview.short_description = "Image"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "comment_preview", "image_preview")

    def comment_preview(self, obj):
        return obj.comment[:50] + "..." if len(obj.comment) > 50 else obj.comment

    comment_preview.short_description = "Comment"

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="border-radius:5px;" />'
        return "-"

    image_preview.allow_tags = True
    image_preview.short_description = "Image"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category",)


@admin.register(ClientImage)
class ClientImageAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "image_preview")
    list_filter = ("client",)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="border-radius:5px;" />'
        return "-"

    image_preview.allow_tags = True
    image_preview.short_description = "Image"

admin.site.register(FAQ)

admin.site.register(Home)

admin.site.register(About)