from django.contrib.auth import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

#
# class User(AbstractUser):
#     """
#     Default custom user model for {{cookiecutter.project_name}}.
#     If adding fields that need to be filled at user signup,
#     check forms.SignupForm and forms.SocialSignupForms accordingly.
#     """
#
#     #: First and last name do not cover name patterns around the globe
#     email = CharField(
#         _("email"),
#         max_length=150,
#         unique=True,
#         help_text=_(
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
#         ),
#         # validators=[email_validator],
#         error_messages={
#             "unique": _("A user with that email already exists."),
#         },
#     )
#
#     def get_absolute_url(self):
#         """Get url for user's detail view.
#         Returns:
#             str: URL for user detail.
#         """
#         return reverse("users:detail", kwargs={"email": self.email})
