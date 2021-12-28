from django.contrib import admin

# Register your models here.
from .models import Artist, Store, Gallery, Assistant


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    # exclude = "slug"
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Assistant)
admin.site.register(Artist)
admin.site.register(Gallery)
