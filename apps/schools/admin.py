from django.contrib import admin

from .models import School


class SchoolModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created"]
    list_filter = ["created"]
    search_fields = ["name"]

    class Meta:
        model = School


admin.site.register(School, SchoolModelAdmin)
