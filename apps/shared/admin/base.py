from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import Permission
from django.contrib.sites.models import Site
from unfold.admin import ModelAdmin
from unfold.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(Site)
try:
    admin.site.unregister(Permission)
except NotRegistered:
    pass


@admin.register(Permission)
class PermissionAdmin(ModelAdmin):
    list_display = ("id", "name", "content_type", "codename")
    search_fields = ("name", "codename")
    ordering = ("content_type__app_label", "codename")
    list_filter = ("content_type",)
    autocomplete_fields = ("content_type",)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    filter_vertical = ("permissions",)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    change_password_form = AdminPasswordChangeForm
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ("id", "username", "email", "is_active", "is_staff", "is_superuser")
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("username",)
    list_editable = ("is_active", "is_staff", "is_superuser")
    filter_vertical = ("groups", "user_permissions")


@admin.register(Site)
class SiteAdmin(ModelAdmin):
    list_display = ("id", "domain", "name")
    search_fields = ("domain", "name")
    ordering = ("domain",)
