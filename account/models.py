from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):
    phone_validator = RegexValidator(regex=r'^\+?3?8?[- 0]?[- (]?[- 0(]?[0-9]{2}\)?([ -]?[0-9]){7}',
                                     message='Enter phone in format +380XXXXXXXXX')

    phone = models.CharField(max_length=20, validators=[phone_validator], blank=True)
