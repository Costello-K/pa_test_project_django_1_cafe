import os
import uuid

from django.db import models
from django.core.validators import RegexValidator
from django_google_maps import fields as map_fields


class NewFileName:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_file_name(self, obj, file_name):
        ext = file_name.strip().split('.')[-1]
        file_name = f'{uuid.uuid4()}.{ext}'
        return os.path.join(f'{self.filepath}', file_name)


class StartPage(models.Model):
    position = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    photo = models.FileField(upload_to=NewFileName('images/start_page').get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}: {self.description[:20]}'

    class Meta:
        ordering = ('position', )


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    video = models.FileField(upload_to=NewFileName('video/about').get_file_name)
    photo = models.ImageField(upload_to=NewFileName('images/about').get_file_name)

    def __str__(self):
        return f'{self.title}: {self.description[:20]}'


class WhyUsCard(models.Model):
    position = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}: {self.position}'

    class Meta:
        ordering = ('position', )


class DishCategory(models.Model):
    position = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class Dish(models.Model):
    position = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=NewFileName('images/dishes').get_file_name)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', )


class Events(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=600)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to=NewFileName('images/events').get_file_name)
    is_visible = models.BooleanField(default=True)
    date_stop_event = models.DateTimeField()

    def __str__(self):
        return f'{self.title}: {self.date_stop_event}'

    class Meta:
        ordering = ('date_stop_event', )


class RestaurantPhoto(models.Model):
    position = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to=NewFileName('images/restaurant').get_file_name)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position', )


class Chefs(models.Model):
    position = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=NewFileName('images/chefs').get_file_name)
    is_visible = models.BooleanField(default=True)
    link_twitter = models.URLField(blank=True)
    link_facebook = models.URLField(blank=True)
    link_instagram = models.URLField(blank=True)
    link_linkedin = models.URLField(blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}. {self.profession.title()}'

    class Meta:
        ordering = ('position', )


class Review(models.Model):
    position = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, blank=True)
    profession = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to=NewFileName('images/review').get_file_name, blank=True)
    is_visible = models.BooleanField(default=True)
    rating = models.CharField(max_length=5, choices=(('1' * i, i) for i in range(1, 6)))
    date_review = models.DateTimeField()
    message = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}. Rating: {self.rating}'

    class Meta:
        ordering = ('date_review', )


class UserReservation(models.Model):
    phone_validator = RegexValidator(regex=r'^\+?3?8?[- 0]?[- (]?[- 0(]?[0-9]{2}\)?([ -]?[0-9]){7}',
                                     message='Enter phone in format +380XXXXXXXXX')
    email_validator = RegexValidator(regex=r'[\da-zA-Z](-?[_\da-zA-Z])*-?@([\da-zA-Z]+\.)*[a-z]{2,6}',
                                     message='Enter a valid email address')
    date_validator = RegexValidator(regex=r'\d{2,4}([- ,.]\d{1,2}){2}', message='Enter date in format "0000-00-00"')
    time_validator = RegexValidator(regex=r'\d{2}[:-]\d{2}', message='Enter time in format "00:00"')

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, blank=True, validators=[email_validator])
    phone = models.CharField(max_length=20, validators=[phone_validator])
    persons = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    manager_date_processed = models.DateTimeField(auto_now=True)
    is_processed = models.BooleanField(default=False)
    future_date_reserve = models.DateField(validators=[date_validator])
    future_time_reserve = models.TimeField(validators=[time_validator])

    def __str__(self):
        return f'"{self.name}" {self.phone}: {self.message[:20]}'

    class Meta:
        ordering = ('-date', )


class UserMessage(models.Model):
    email_validator = RegexValidator(regex=r'[\da-zA-Z](-?[_\da-zA-Z])*-?@([\da-zA-Z]+\.)*[a-z]{2,6}',
                                     message='Enter a valid email address')
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, validators=[email_validator])
    subject_message = models.TextField(max_length=100)
    message = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    manager_date_processed = models.DateTimeField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'"{self.message[:50]}'

    class Meta:
        ordering = ('-date', )


# class Maps(models.Model):
#     address = map_fields.AddressField(max_length=200)
#     geolocation = map_fields.GeoLocationField(max_length=100)
