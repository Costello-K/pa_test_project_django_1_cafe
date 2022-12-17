from django.db import models
import uuid
import os


# Create your models here.
class About(models.Model):

    @staticmethod
    def get_file_name(filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('video/about', filename)

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    video = models.FileField(upload_to=get_file_name)


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

    @staticmethod
    def get_file_name(filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes', filename)

    position = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    description = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class Events(models.Model):

    @staticmethod
    def get_file_name(filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/events', filename)

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
    date_stop_event = models.DateTimeField()

    def __str__(self):
        return f'{self.title}: {self.date_stop_event}'

    class Meta:
        ordering = ('date_stop_event', )
