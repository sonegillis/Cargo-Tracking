from django.contrib import admin
from .models import Package
# Register your models here.

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    readonly_fields = ["package_id"]
