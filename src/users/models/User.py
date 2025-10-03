from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    email = models.EmailField(
        _("email address"),
        unique=True,
        blank=False,
    )

    image = models.ImageField(
        blank=True,
        null=True,
        upload_to="ProfileImages/",
    )

    phone_number = PhoneNumberField(
        unique=True,
        region="FR",
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
