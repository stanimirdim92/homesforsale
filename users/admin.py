from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from django.utils.translation import gettext_lazy as _

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Address, User as UserCustom

User: UserCustom = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = User

    list_display = ("id", "email", "title", "name_first", "name_last", "entity_type", "company_name", "is_staff", "is_active", "is_superuser")
    list_filter = ("is_staff", "is_active", "is_superuser", "groups", "entity_type")
    readonly_fields = ("time_created", 'time_modified', 'uuid', "id")
    search_fields = ["email", "name_first", "name_last", "uuid", "id", "entity_type", "company_name"]
    ordering = ("id", "email", "name_first", "name_last", "entity_type", "company_name")

    fieldsets = (
        (_('Personal info'), {
                "fields": (
                    ("title"),
                    "name_first",
                    "name_middle",
                    "name_last",
                    "company_name",
                )
            }),
        ( _("Details"), {
                "fields": (
                    "id",
                    "uuid",
                    "entity_type",
                    "phone_number",
                    "timezone",
                    "language",
                    "currency",
                )
            }),
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
        (_("Dates"), {
            "fields": (
                "time_modified",
                "time_created",
                "time_deleted",
            )
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'address_line_1', 'city', 'state', 'postal_code', 'country')
