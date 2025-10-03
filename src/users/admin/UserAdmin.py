from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from src.users.models.User import User


class UserAdmin(UserAdmin):

    model = User

    list_display = (
        "email",
        "username",
        "image",
        "phone_number",
    )

    fieldsets = (
        (
            "User details",
            {
                "fields": (
                    "email",
                    "username",
                    "password",
                    "image",
                    "phone_number",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            "User Details",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "image",
                    "phone_number",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
