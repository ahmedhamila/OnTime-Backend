from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from src.utils.models.BaseModel import BaseModel


class Employee(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique=True, region="FR")
    pin_code = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
