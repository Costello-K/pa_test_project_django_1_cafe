from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    phone_validator = RegexValidator(regex=r'^\+?3?8?[- 0]?[- (]?[- 0(]?[0-9]{2}\)?([ -]?[0-9]){7}',
                                     message='Enter phone in format +380XXXXXXXXX')

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=20, validators=[phone_validator], verbose_name='Phone', blank=True)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
