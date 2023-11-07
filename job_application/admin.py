from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date", "occupation")
    list_filter = ("date", "occupation")
    readonly_fields = ("occupation",)
    ordering = ("last_name", "date")
    search_fields = ("last_name", "date")


admin.site.register(Form, FormAdmin)
