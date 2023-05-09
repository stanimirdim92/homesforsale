from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser, PermissionsMixin):
    username = None
    date_joined = None
    first_name = None
    last_name = None

    email = models.EmailField(
        _("email"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        # validators=[username_validator],
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    name_first = models.CharField(_("first name"), max_length=128, blank=False)
    name_last = models.CharField(_("last name"), max_length=128, blank=True,null=True)
    company_name = models.CharField(_("company name"), max_length=128, blank=True,null=True)
    uuid = models.UUIDField(_("uuid"), max_length=36, unique=True)
    time_created = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
