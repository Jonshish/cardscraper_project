from django.contrib import admin

from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "sold_price", "sold_date")
    list_display_links = ("id", "title")
    list_filter = ("sold_date",)
    search_fields = ("title", "sold_price", "sold_date")


admin.site.register(Data, DataAdmin)
