from django.contrib import admin
from .models import Bank
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Bank)
class ViewAdmin(ImportExportActionModelAdmin):
    pass

