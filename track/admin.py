from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from .models import Package
# Register your models here.


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    readonly_fields = ["package_id"]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '500'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }
