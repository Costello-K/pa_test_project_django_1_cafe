# Generated by Django 4.1.4 on 2022-12-27 05:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0014_alter_about_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreservation',
            name='future_date_reserve',
            field=models.DateField(validators=[django.core.validators.RegexValidator(message='Enter date in format "0000-00-00"', regex='\\d{2,4}([ -,.]{1,2}){2}')]),
        ),
    ]
