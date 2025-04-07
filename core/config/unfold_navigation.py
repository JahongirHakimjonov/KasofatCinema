from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def user_has_group_or_permission(user, permission):
    if user.is_superuser:
        return True

    group_names = user.groups.values_list("name", flat=True)
    if not group_names:
        return True

    return user.groups.filter(permissions__codename=permission).exists()


PAGES = [
    {
        "seperator": True,
        "items": [
            {
                "title": _("Bosh sahifa"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Foydalanuvchilar"),
        "items": [
            {
                "title": _("Guruhlar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:auth_group_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_group"
                ),
            },
            {
                "title": _("Foydalanuvchilar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:auth_user_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_user"
                ),
            },
            {
                "title": _("Permissions"),
                "icon": "person_add",
                "link": reverse_lazy("admin:auth_permission_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_user"
                ),
            },
            {
                "title": _("Site"),
                "icon": "language",
                "link": reverse_lazy("admin:sites_site_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_sites"
                ),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Bot"),
        "items": [
            {
                "title": _("Bot Users"),
                "icon": "person_add",
                "link": reverse_lazy("admin:backend_botuser_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_botuser"
                ),
            },
            {
                "title": _("Subscribing Channels"),
                "icon": "admin_panel_settings",
                "link": reverse_lazy("admin:backend_subscribechannel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_subscribechannel"
                ),
            },
            {
                "title": _("Settings"),
                "icon": "toggle_on",
                "link": reverse_lazy("admin:backend_settings_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_settings"
                ),
            },
            {
                "title": _("News"),
                "icon": "brand_awareness",
                "link": reverse_lazy("admin:backend_news_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_news"
                ),
            },
            {
                "title": _("Info"),
                "icon": "info",
                "link": reverse_lazy("admin:backend_info_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_info"
                ),
            },
            {
                "title": _("Saved"),
                "icon": "bookmark",
                "link": reverse_lazy("admin:backend_saved_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_saved"
                ),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Models"),
        "items": [
            {
                "title": _("Cinema"),
                "icon": "movie",
                "link": reverse_lazy("admin:backend_cinema_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_cinema"
                ),
            },
            {
                "title": _("Channel"),
                "icon": "campaign",
                "link": reverse_lazy("admin:backend_channel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_channel"
                ),
            },
            {
                "title": _("Resolution"),
                "icon": "4k",
                "link": reverse_lazy("admin:backend_resolution_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_resolution"
                ),
            },
            {
                "title": _("Country"),
                "icon": "public",
                "link": reverse_lazy("admin:backend_country_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_country"
                ),
            },
            {
                "title": _("Genre"),
                "icon": "checklist_rtl",
                "link": reverse_lazy("admin:backend_genre_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_genre"
                ),
            },
            {
                "title": _("Year"),
                "icon": "edit_calendar",
                "link": reverse_lazy("admin:backend_year_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_year"
                ),
            },
        ],
    },
]

TABS = [
    {
        "models": [
            "auth.user",
            "auth.group",
        ],
        "items": [
            {
                "title": _("Foydalanuvchilar"),
                "link": reverse_lazy("admin:auth_user_changelist"),
            },
            {
                "title": _("Guruhlar"),
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
]
