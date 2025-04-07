from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RangeDateFilter
from unfold.decorators import display

from apps.backend.models.bot import BotUser, LanguageChoices, RoleChoices


@admin.register(BotUser)
class BotUsersAdmin(ModelAdmin):
    list_display = (
        "id",
        "telegram_id_with_color",
        "username",
        "language_code_with_color",
        "role_with_color",
        "is_active",
        "created_at",
    )
    search_fields = (
        "telegram_id",
        "username",
        "first_name",
        "last_name",
        "phone",
        "full_name",
    )
    list_filter = (
        ("created_at", RangeDateFilter),
        "is_active",
        "role",
        "language_code",
    )
    list_filter_submit = True
    list_display_links = ("id", "telegram_id_with_color", "username")

    @display(
        description=_("Language"),
        label={
            LanguageChoices.UZ: "info",
            LanguageChoices.RU: "info",
            LanguageChoices.EN: "info",
        },
    )
    def language_code_with_color(self, obj):
        return obj.language_code, obj.get_language_code_display()

    @display(
        description=_("Role"),
        label={
            RoleChoices.USER: "info",
            RoleChoices.MODERATOR: "success",
            RoleChoices.ADMIN: "primary",
        },
    )
    def role_with_color(self, obj):
        return obj.role, obj.get_role_display()

    @display(description=_("Telegram ID"), label=True)
    def telegram_id_with_color(self, obj):
        return obj.telegram_id
