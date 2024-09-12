import uuid as uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.reverse import reverse

from users.enums import Titles, Types, Language
from users.managers import UserManager


class User(AbstractUser):
    username = None  # type: ignore
    date_joined = None  # type: ignore
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    last_login = None  # type: ignore

    email = models.EmailField(
        _("email"),
        max_length=150,
        unique=True,
        db_index=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[validate_email],
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    title = models.CharField(_("title"), max_length=10, blank=True, null=True, choices=Titles.choices(), default=Titles.MR)
    name_first = models.CharField(_("first name"), max_length=128, blank=False, null=True)
    name_middle = models.CharField(_("middle name"), max_length=128, blank=True, null=True)
    name_last = models.CharField(_("last name"), max_length=128, blank=True, null=True)

    company_name = models.CharField(_("company name"), max_length=128, blank=True, null=True)
    company_vat_number = models.CharField(_("vat number"), max_length=128, blank=True, unique=False, null=True)

    phone_number = PhoneNumberField(null=True, blank=True, unique=False, default=None)
    uuid = models.UUIDField(_("uuid"), max_length=36, unique=True, default=uuid.uuid4, editable=False, null=True)

    time_created = models.DateTimeField(_("created at"), auto_now_add=True)
    time_modified = models.DateTimeField(_("modified at"), auto_now=True)
    time_deleted = models.DateTimeField(_("deleted at"), blank=True, null=True)

    reference = models.CharField(_("reference"), max_length=128, blank=False, unique=True, default=None)
    reference_external = models.CharField(_("reference external"), max_length=128, blank=True, unique=False, null=True)
    entity_type = models.CharField(_("type"), max_length=128, blank=True, unique=False, null=True, default=Types.CLIENT, choices=Types.choices())

    language = models.CharField(_("language"), max_length=2, blank=True, null=True, choices=Language.choices(), default=Language.EN)
    currency = models.CharField(_("currency"), max_length=3, blank=True, null=True)
    timezone = models.CharField(_("timezone"), max_length=128, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name_first', 'name_last']

    objects = UserManager()

    """
        Main method to save and create users, even with manage.py
    """

    def save(self, *args, **kwargs):
        return super().save(args, kwargs)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self) -> str:
        return reverse("user-detail", args=[str(self.uuid)])

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s %s" % (self.name_first, self.name_middle, self.name_last)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.name_first


class Address(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True, on_delete=models.CASCADE, related_name='addresses')

    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    id = models.UUIDField(_("id"), primary_key=True, max_length=36, unique=True, default=uuid.uuid4, editable=False)

    time_created = models.DateTimeField(_("created at"), auto_now_add=True)
    time_modified = models.DateTimeField(_("modified at"), auto_now=True)
    time_deleted = models.DateTimeField(_("deleted at"), blank=True, null=True)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}, {self.country}"
