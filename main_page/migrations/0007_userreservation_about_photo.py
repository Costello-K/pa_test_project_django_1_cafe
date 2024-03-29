# Generated by Django 4.1.4 on 2022-12-21 01:34

import django.core.validators
from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_alter_review_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=70, validators=[django.core.validators.RegexValidator(message='Enter a valid email address', regex='[\\da-zA-Z](-?[_\\da-zA-Z])*-?@([\\da-zA-Z]+\\.)*[a-z]{2,6}')])),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number', regex='\\+?3?8?[ -(]?0 ?\\(?\\d{2}\\)?([ -]?\\d{7})')])),
                ('persons', models.PositiveSmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('manager_date_processed', models.DateTimeField(auto_now=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.AddField(
            model_name='about',
            name='photo',
            field=models.ImageField(default=None, upload_to=main_page.models.NewFileName.get_file_name),
            preserve_default=False,
        ),
    ]
