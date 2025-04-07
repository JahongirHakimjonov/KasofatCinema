from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.backend.models.settings import Settings


@admin.register(Settings)
class SettingsAdmin(ModelAdmin, ImportExportModelAdmin, TabbedTranslationAdmin):
    list_display = ["id", "label", "value"]
    list_editable = ["value"]
    search_fields = ["key", "label"]
    list_per_page = 50
    list_filter = ["value"]
