from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from django.utils.translation import gettext_lazy as _

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Address

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm
    model = User
#
#     list_display = ("email", "name_first", "is_staff", "is_active",)
#     list_filter = ("email", "is_staff", "is_active",)
#     readonly_fields = ("time_created", 'time_modified','uuid')
#
#     fieldsets = (
#         (_('Personal info'), {"fields": ("title","name_first","name_middle","name_last",)}),
#         (None, {"fields": ("reference","reference_external","company_vat_number","entity_type","email", "password")}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (_("Important dates"), {"fields": ("time_modified","time_created","time_deleted",)}),
#     )
#     search_fields = ["email", "name_first", "name_middle", "name_last"]
    ordering = ["id"]
#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": (
#                 "email", "password", "password1", "password2", "is_staff",
#                 "is_active","groups","user_permissions"
#             )}
#         ),
#     )

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'address_line_1', 'city', 'state', 'postal_code', 'country')
