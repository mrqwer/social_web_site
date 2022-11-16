from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

#@admin.register(CustomUser)

class AuthorAdmin(UserAdmin):
    list_display = ("username", "email", "phone", "first_name", "last_name", "is_staff")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "middle", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (('info', {'fields': ("phone", "avatar", "gender")}))
    )
admin.site.register(CustomUser, AuthorAdmin)
