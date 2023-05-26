import uuid as uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.reverse import reverse

from .managers import UserManager


def generate_reference(entity_type: str | None = None) -> str:
    prefix = (entity_type or User.Types.CLIENT)[0] + timezone.now().strftime('%y')

    counter = User.objects.filter(reference__startswith=prefix).count()

    reference = prefix + str(counter + 1)
    has_reference = User.objects.filter(reference=reference).exists()

    while has_reference:
        counter += 1
        reference = prefix + str(counter)
        has_reference = User.objects.filter(reference=reference).exists()

    return reference


class User(AbstractUser):
    class Types(models.TextChoices):
        CLIENT = 'CLIENT'
        AGENCY = 'AGENCY'
        ORGANIZATION = 'ORGANIZATION'

    class Titles(models.TextChoices):
        MR = 'Mr'
        MRS = 'Mrs'
        MISS = 'Miss'
        MS = 'Ms'
        DR = 'Dr'
        PROF = 'Prof'
        SIR = 'Sir'

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

    title = models.CharField(_("title"), max_length=10, blank=True, null=True, choices=Titles.choices, default=Titles.MR)
    name_first = models.CharField(_("first name"), max_length=128, blank=False, null=True)
    name_middle = models.CharField(_("middle name"), max_length=128, blank=True, null=True)
    name_last = models.CharField(_("last name"), max_length=128, blank=True, null=True)
    company_name = models.CharField(_("company name"), max_length=128, blank=True, null=True)
    uuid = models.UUIDField(_("uuid"), max_length=36, unique=True, default=uuid.uuid4, editable=False, null=True)
    time_created = models.DateTimeField(_("created at"), auto_now_add=True)
    time_modified = models.DateTimeField(_("modified at"), auto_now=True)
    time_deleted = models.DateTimeField(_("deleted at"), blank=True, null=True)
    reference = models.CharField(_("reference"), max_length=128, blank=False, unique=True, default=generate_reference)
    reference_external = models.CharField(_("reference external"), max_length=128, blank=True, unique=False, null=True)
    company_vat_number = models.CharField(_("vat number"), max_length=128, blank=True, unique=False, null=True)
    entity_type = models.CharField(_("type"), max_length=128, blank=True, unique=False, null=True, default=Types.CLIENT, choices=Types.choices)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    """
        Main method to save and create users, even with manage.py
    """

    def save(self, *args, **kwargs):
        # self.reference = generate_reference(getattr(self, 'entity_type'))
        return super().save(args, kwargs)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self) -> str:
        return reverse("user-detail", args=[str(self.uuid)])
