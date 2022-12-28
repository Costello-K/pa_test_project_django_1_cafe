# Generated by Django 4.1.4 on 2022-12-21 04:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0009_userreservation_future_date_reserve_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreservation',
            name='future_date_reserve',
            field=models.DateField(validators=[django.core.validators.RegexValidator(message='Enter date in format "0000-00-00"', regex='\\d{2,4}\\d[ -,.]{1,2}[ -,.]\\d{1,2}')]),
        ),
        migrations.AlterField(
            model_name='userreservation',
            name='future_time_reserve',
            field=models.TimeField(validators=[django.core.validators.RegexValidator(message='Enter time in format "00:00"', regex='\\d{2}[:-]\\d{2}')]),
        ),
    ]