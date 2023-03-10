from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserGender:
    MALE = "male"
    FEMALE = "female"
    NO_SAY = "no_say"

    GENDERS = [
        (MALE, _("Male")),
        (FEMALE, _("Female")),
        (NO_SAY, _("Prefer to not say")),
    ]


class User(AbstractUser):

    USERNAME_FIELD = "username"

    # Personal information
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), blank=False)
    gender = models.CharField(choices=UserGender.GENDERS, blank=False, default=UserGender.NO_SAY, max_length=32)
    # TODO: birthday, country, preferred_lang

    # Site specific information
    is_seller = models.BooleanField(
        default=False, db_index=True, help_text="Whether this user publish content in the site"
    )
    is_test_user = models.BooleanField(default=False, help_text="Whether this user is used for test")
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.get_username()

    def set_is_seller(self) -> None:
        self.is_seller = True
        self.save()
