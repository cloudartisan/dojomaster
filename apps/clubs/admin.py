from django.contrib import admin

from .models import Club


class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_created', 'url', 'phone', 'mobile', 'fax']
    list_filter = ['date_created']
    search_fields = ['name']

    class Meta:
        model = Club


admin.site.register(Club, ClubAdmin)
