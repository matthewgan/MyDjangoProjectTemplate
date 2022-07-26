from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "business", "last_update")


admin.site.register(Company, CompanyAdmin)
