from django.contrib import admin

from .models import Club


class ClubModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created"]
    list_filter = ["created"]
    search_fields = ["name"]

    class Meta:
        model = Club


admin.site.register(Club, ClubModelAdmin)
