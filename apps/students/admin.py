from django.contrib import admin

from .models import Student, Contact


class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "joined"]
    list_filter = ["joined"]
    search_fields = ["first_name", "last_name"]

    class Meta:
        model = Student


class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "mobile_phone"]
    search_fields = ["first_name", "last_name"]

    class Meta:
        model = Contact


admin.site.register(Student, StudentAdmin)
admin.site.register(Contact, ContactAdmin)
