import enum
import uuid as uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import validate_email
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


def generate_reference():

    prefix = User.Types.CLIENT+timezone.now().strftime('%y')

    counter = User.objects.filter(reference__startswith=prefix).count()

    reference = prefix + str(counter + 1)
    has_reference = User.objects.filter(reference=reference).exists()

    while has_reference:
        counter += 1
        reference = prefix + str(counter)
        has_reference = User.objects.filter(reference=reference).exists()

    return reference


class User(AbstractUser, PermissionsMixin):
    class Types(models.TextChoices):
        CLIENT = 'C'
        AGENCY = 'A'


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

    title = models.CharField(_("title"), max_length=10, blank=True, null=True)
    name_first = models.CharField(_("first name"), max_length=128, blank=False, null=True)
    name_middle = models.CharField(_("middle name"), max_length=128, blank=True, null=True)
    name_last = models.CharField(_("last name"), max_length=128, blank=True, null=True)
    company_name = models.CharField(_("company name"), max_length=128, blank=True, null=True)
    uuid = models.UUIDField(_("uuid"), max_length=36, unique=True, default=uuid.uuid4, editable=False, null=True)
    time_created = models.DateTimeField(_("created at"), auto_now_add=True)
    time_modified = models.DateTimeField(_("modified at"), auto_now=True)
    time_deleted = models.DateTimeField(_("deleted at"), blank=True, null=True)
    reference = models.CharField(_("reference"), max_length=128, blank=False, unique=True, default=generate_reference)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    """
        Main method to save and create users, even with manage.py
    """
    def save(self, *args, **kwargs):
        return super().save(args, kwargs)

    def __str__(self):
        return self.email

    # def get_absolute_url(self) -> str:
    #     """Get URL for user's detail view.
    #
    #     Returns:
    #         str: URL for user detail.
    #
    #     """
    #     return reverse("users:detail", kwargs={"pk": self.id})
